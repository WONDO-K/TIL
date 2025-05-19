# Spring에서 객체를 Bean으로 관리하는 이유는?
- 애플리케이션의 설계, 확장성, 유지보수 측면에서 많은 이점을 제공하기 떄문이다.

1. 의존성 관리 자동화
- 빈으로 등록된 객체들은 Spring 컨테이너(BeanFactory, ApplicationContext)가 자동으로 의존성을 주입해준다.
- 개발자가 직접 객체를 생성하고 의존성을 연결할 필요가 없어진다.
- 컨테이너가 빌드 시점에 순환 의존성을 감지하여 설계 오류를 조기에 발견할 수 있다.
```java
@Service
class OrderService(
    private val productRepository: ProductRepository,  // 자동 주입
    private val paymentGateway: PaymentGateway        // 자동 주입
)
```

2. 싱글톤 패턴 구현
- 기본적으로 Spring은 싱글톤으로 관리하여 메모리 사용을 최적화하고, 불필요한 객체 생성을 방지한다.
```java
// 아래 두 userRepository는 동일한 인스턴스
@Service
class UserService(private val userRepository: UserRepository)

@Service
class AuthService(private val userRepository: UserRepository)
```

3. 생명주기 관리
- Spring은 빈의 초기화와 소멸 과정을 자동으로 관리한다.
- 이를 통해 리소스 할당 및 해제를 체계적으로 처리할 수 있다.
- 아래의 코드는 개발자가 개입하여 초기화/정리 작업을 추가하고 싶을때 사용할 수 있음.
    - 외부 api 연결 초기화.
        - API 요청마다 새로 연결하지 않고, 이미 만들어진 연결(소켓/세션)을 계속 사용하는 구조
        - 초기화라함은 앱 시작시 외부 API 서버와의 통신을 위한 객체 (Client, Token, Session 등)을 미리 만들어 두는 것이다.
    - 미리 캐시 로딩하기.
        - 미리 캐시 로딩은 실시간 요청 시 DB를 매번 조회하지 않게 하여 성능을 향상시키는 데 목적을 둔다.
```java
@Component
class DatabaseConnection {
    @PostConstruct
    fun initialize() {
        // 초기화 로직
    }
    
    @PreDestroy
    fun cleanup() {
        // 리소스 정리 로직
    }
}
```

4. AOP(관점 지향 프로그래밍)
- 빈으로 관리되는 객체들은 트랜잭션 관리, 로깅, 보안 등의 공통 관심사를 쉽게 적용할 수 있다.
```java
@Service
class TransferService(private val accountRepository: AccountRepository) {
    @Transactional  // AOP를 통한 트랜잭션 관리
    fun transferMoney(from: String, to: String, amount: BigDecimal) {
        // 송금 로직
    }
}
```

5. 테스트 용이성
- 빈으로 관리되는 컴포넌트는 모킹(mocking)이나 테스트용 구현체로 쉽게 대처할 수 있어 단위 테스트와 통합 테스트가 용이하다.
```java
@SpringBootTest
class UserServiceTest {
    @MockBean
    lateinit var userRepository: UserRepository
    
    @Autowired
    lateinit var userService: UserService
    
    @Test
    fun testGetUser() {
        // given
        val userId = 1L
        whenever(userRepository.findById(userId)).thenReturn(User(userId, "Test User"))
        
        // when
        val result = userService.getUser(userId)
        
        // then
        assertEquals("Test User", result.name)
    }
}
```

6. 설정의 중앙화
- 애플리케이션의 구성 요소들을 Bean으로 관리함으로써 설정을 중앙화하고 일관된 방식으로 관리할 수 있다.
```java
@Configuration
class AppConfig {
    @Bean
    fun dataSource(): DataSource {
        return HikariDataSource().apply {
            jdbcUrl = "jdbc:postgresql://localhost:5432/mydb"
            username = "user"
            password = "password"
            maximumPoolSize = 10
        }
    }
}
```