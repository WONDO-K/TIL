# Spring WebFlux 개요

1. **정의**  
Spring WebFlux는 비동기 논블로킹 웹 프레임워크로, Reactive Streams 기반(Project Reactor)이며 I/O-bound 환경에 최적화되어 동시성을 높인다.

2. **특징**
   - Netty, Undertow 등 논블로킹 서버 기반
   - 적은 스레드로 많은 요청 처리 (Event Loop)
   - Publisher/Subscriber 패턴 사용

3. **동시성과 병렬성**
   - WebFlux는 기본적으로 동시성(Concurrency)에 특화
   - CPU-bound 작업은 기본 Event Loop에서 병목이 생길 수 있어, `publishOn(Schedulers.parallel())` 또는 `subscribeOn(Schedulers.boundedElastic())`로 병렬성(Parallelism) 확보 가능
   - 즉, WebFlux는 동시성과 병렬성을 조합 가능하지만 병렬성은 별도 설계가 필요

4. **실무 활용 예시**
   - 수백~수천 건의 요청을 논블로킹으로 처리하며, 데이터 변환·AI inference 같은 CPU 연산은 병렬 스레드풀로 위임

5. **코드 예시**
   ```java
   Mono.just(data)
       .publishOn(Schedulers.parallel()) // 병렬 스레드 풀 사용
       .map(this::heavyComputation)
       .subscribe(result -> log.info("결과: {}", result));
   ```

# 📌 WebFlux 도입 시 주의점

1. **"MVC보다 무조건 성능이 좋다"는 오해 정리**  
   WebFlux가 항상 MVC보다 빠르거나 효율적인 것은 아니다. WebFlux는 I/O-bound, 논블로킹 환경에 적합하며 CPU-bound 작업에서는 오히려 복잡도가 증가할 수 있다.

2. **WebFlux가 필요한 경우와 불필요한 경우 구분**  
   - 필요한 경우: 외부 API 호출이 많거나, 대량의 동시 요청 처리, 논블로킹 I/O가 중요한 서비스  
   - 불필요한 경우: 단순 CRUD, CPU 연산 중심, 적은 동시성 요구 서비스

3. **YAGNI/KISS/오버엔지니어링 회피 원칙**  
   복잡한 Reactive 프로그래밍은 유지보수와 가독성을 떨어뜨릴 수 있으므로, 실제 필요에 따라 도입 여부를 신중히 결정해야 한다.

4. **잘못된 도입 예시**  
   - 외부 API 5~20개를 동시에 호출하는 경우 스레드 및 메모리 계산이 복잡해지고, 오히려 성능 저하 발생 가능  
   - 대안: 적절한 동기 호출과 캐싱, 스레드 풀 조절 등으로 간단하게 해결 가능

5. **기술 선택 시 고려 요소**  
   - 운영 복잡도 증가 여부  
   - 개발 및 유지보수 비용  
   - 팀의 역량과 경험  

# Spring WebFlux

# 💬 면접 대비 포인트

- MVC와 WebFlux의 차이점: 동기 vs 비동기, 블로킹 vs 논블로킹, 적합한 사용 사례  
- WebFlux를 꼭 써야 하는 상황: 높은 동시성, 많은 외부 API 호출, I/O-bound 서비스  
- 외부 API 호출이 많은 서비스에서 WebFlux 사용 여부 판단 기준  
- WebFlux 대신 다른 방법(예: 스레드 풀 조절, 캐싱) 사용 경험과 그 이유 설명
