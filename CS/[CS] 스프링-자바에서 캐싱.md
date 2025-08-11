# 1) Spring Cache 추상화로 캐시 붙이기 (Caffeine & Redis)
## 1. 의존성
```java
// 공통
implementation "org.springframework.boot:spring-boot-starter-cache"

// 인메모리 캐시(Caffeine)
implementation "com.github.ben-manes.caffeine:caffeine:3.1.8"

// Redis 캐시(원격 캐시)
implementation "org.springframework.boot:spring-boot-starter-data-redis"
```
## 2. 설정(application.yml)
1. (A) Caffeine 인메모리 캐시 — 개발/단일 인스턴스에 가볍게
```java
spring:
  cache:
    type: caffeine
    cache-names: userCache
    caffeine:
      spec: maximumSize=10000,expireAfterWrite=300s  # TTL=300초
```

2. (B) Redis 캐시 — 분산 환경에서의 캐시
```java
spring:
  cache:
    type: redis
  data:
    redis:
      host: localhost
      port: 6379
  # (선택) 캐시 이름별 TTL
  cache:
    redis:
      time-to-live: 300000   # 300s
```

## 3. 캐시 매니저(선택: 커스터마이즈가 필요할 때)
```java
@Configuration
@EnableCaching
public class CacheConfig {

    // Caffeine
    @Bean
    public CacheManager caffeineCacheManager() {
        Caffeine<Object, Object> caffeine = Caffeine.newBuilder()
                .maximumSize(10_000)
                .expireAfterWrite(Duration.ofMinutes(5));
        CaffeineCacheManager mgr = new CaffeineCacheManager("userCache");
        mgr.setCaffeine(caffeine);
        return mgr;
    }

    // Redis (원한다면 위 대신 사용)
    // @Bean
    // public CacheManager redisCacheManager(RedisConnectionFactory cf) {
    //     return RedisCacheManager.builder(cf)
    //             .withCacheConfiguration("userCache",
    //               RedisCacheConfiguration.defaultCacheConfig()
    //                 .entryTtl(Duration.ofMinutes(5)))
    //             .build();
    // }
}
```

4. 서비스 코드
```java
@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository userRepository;

    // 읽기: Cache-Aside 동작 (@Cacheable)
    @Cacheable(cacheNames = "userCache", key = "#userId")
    public UserDto getUser(Long userId) {
        // 캐시에 없으면 여기 로직 실행 → DB 조회 후 결과를 캐시에 저장
        return userRepository.findById(userId)
                .map(UserDto::from)
                .orElseThrow(() -> new NoSuchElementException("user not found"));
    }

    // 쓰기: DB 갱신하면서 캐시도 최신화 (@CachePut = write-through 느낌)
    @CachePut(cacheNames = "userCache", key = "#cmd.id")
    public UserDto updateUser(UpdateUserCommand cmd) {
        User user = userRepository.findById(cmd.id()).orElseThrow();
        user.setName(cmd.name());
        user.setEmail(cmd.email());
        return UserDto.from(userRepository.save(user));  // 반환값이 캐시에 덮어씀
    }

    // 삭제/무효화: 데이터 변경 트리거로 캐시 비우기 (@CacheEvict)
    @CacheEvict(cacheNames = "userCache", key = "#userId")
    public void deleteUser(Long userId) {
        userRepository.deleteById(userId);
    }
}
```
- 언제 어떤 어노테이션?
	-	@Cacheable : 읽기 캐싱(Cache‑Aside). miss 시 메서드 실행→결과 캐시 저장
	-	@CachePut : 업데이트 시 캐시 최신화(write‑through 느낌). 메서드 실행 결과를 항상 캐시에 반영
	-	@CacheEvict : 캐시 무효화. DB 변경/삭제 후 캐시 날려서 불일치 최소화

TTL은 application.yml에서 캐시별로 관리 (데이터 신선도 vs 적중률 트레이드오프).

# 2. 수동 Cache‑Aside (RedisTemplate 사용) — 세밀 제어가 필요할 때
1. 코드
```java
@Service
@RequiredArgsConstructor
public class ProductService {
    private final RedisTemplate<String, ProductDto> redisTemplate;
    private final ProductRepository productRepository;

    private String keyOf(long id) { return "product:" + id; }

    public ProductDto getProduct(long id) {
        // 1) 캐시 조회
        ProductDto cached = redisTemplate.opsForValue().get(keyOf(id));
        if (cached != null) return cached;

        // 2) 미스 → DB 조회
        ProductDto dto = productRepository.findById(id)
                .map(ProductDto::from)
                .orElseThrow();

        // 3) 캐시에 저장(예: TTL 5분)
        redisTemplate.opsForValue().set(keyOf(id), dto, Duration.ofMinutes(5));
        return dto;
    }

    // write-through-ish: DB 저장 후 캐시 갱신
    public ProductDto updateProduct(UpdateProductCommand cmd) {
        Product p = productRepository.findById(cmd.id()).orElseThrow();
        p.setName(cmd.name());
        p.setPrice(cmd.price());
        ProductDto saved = ProductDto.from(productRepository.save(p));

        redisTemplate.opsForValue().set(keyOf(cmd.id()), saved, Duration.ofMinutes(5));
        return saved;
    }

    // invalidation: 삭제/강제 무효화
    public void evictProduct(long id) {
        productRepository.deleteById(id);
        redisTemplate.delete(keyOf(id));
    }
}
```
2. 응용 : 캐시 스탬피드 방지(간단 락)
```java
public ProductDto getProduct(long id) {
    String key = keyOf(id);
    ProductDto cached = redisTemplate.opsForValue().get(key);
    if (cached != null) return cached;

    // 분산락 시도 (간단 버전)
    String lockKey = key + ":lock";
    Boolean locked = redisTemplate.opsForValue().setIfAbsent(lockKey, "1", Duration.ofSeconds(3));
    if (Boolean.TRUE.equals(locked)) {
        try {
            ProductDto dto = productRepository.findById(id).map(ProductDto::from).orElseThrow();
            redisTemplate.opsForValue().set(key, dto, Duration.ofMinutes(5));
            return dto;
        } finally {
            redisTemplate.delete(lockKey);
        }
    } else {
        // 잠깐 대기 후 캐시 재조회 (요청 병합 효과)
        try { Thread.sleep(50); } catch (InterruptedException ignored) {}
        ProductDto retry = redisTemplate.opsForValue().get(key);
        if (retry != null) return retry;
        // 그래도 없으면 최후의 방안으로 DB 조회
        return productRepository.findById(id).map(ProductDto::from).orElseThrow();
    }
}
```

3. Write‑Behind 아이디어 스케치
> Spring이 캐시 레벨에서 write‑behind를 바로 제공하진 않는다. 그래도 아래처럼 큐/버퍼 → 비동기 DB 반영으로 유사 패턴을 만들 수는 있다.

```java
@Service
@RequiredArgsConstructor
public class CounterService {
    private final RedisTemplate<String, Long> redis;
    private final CounterRepository repo;

    public void like(String postId) {
        // 캐시에 먼저 쓰기(증가) → 응답 빠름
        redis.opsForValue().increment("like:"+postId, 1L);
        // 비동기 배치 반영
        flushQueueAsync(postId);
    }

    @Async
    public void flushQueueAsync(String postId) {
        // (예시) 일정 주기/임계치마다 합산 후 DB에 반영
        Long current = redis.opsForValue().get("like:"+postId);
        if (current != null) repo.updateLikeCount(postId, current);
    }
}
```
> 운영 주의: 장애 시 유실 방지(Kafka 등 영속 큐, Redis AOF/RDB 설정), 중복 처리 보정, 정합성 임계값을 반드시 설계해야 한다.

## 면접 예상 질문
•	Q. @Cacheable / @CachePut / @CacheEvict 차이와 사용 시점?
    A. 읽기 캐시 / 업데이트 즉시 캐시 동기화 / 캐시 무효화. Cache‑Aside의 읽기·쓰기에 각각 대응.

•	Q. TTL을 어떻게 정하나요?
    A. 데이터 신선도 vs DB부하 트레이드오프. 조회 패턴/변경 빈도/비즈니스 요구(초 단위? 분 단위?)로 결정. 중요 변경엔 이벤트 기반 무효화 병행.

•	Q. 캐시 스탬피드는? 해결책은?
    A. 미스 순간 동시 다발 DB 히트. 분산락, Soft‑TTL, 요청 병합(coalescing), 백오프 재시도 등을 적용.

•	Q. 인메모리(Caffeine) vs Redis 선택 기준?
    A. 단일 인스턴스/초고속 접근은 Caffeine. 멀티 인스턴스/확장/공유는 Redis.