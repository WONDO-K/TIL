# 동기와 비동기의 차이
✅ 동기(Synchronous)와 비동기(Asynchronous)는 함수 호출 시 결과를 기다리는지 여부에 따라 구분한다.
✅ 블로킹(Block)과 논블로킹(Non-Block)은 호출한 스레드가 멈추는지(대기) 여부와 관련된다.

호출하는 함수의 작업 완료를 기다리는지 여부의 차이에 있다.
함수 A가 동기로 함수 B를 호출하면 A는 B의 작업이 완료될 때까지 기다려야 한다.
따라서 작업이 순차적으로 진행된다.
반면, 함수 A가 비동기로 함수 B를 호출하면 A는 B의 작업 완료를 신경쓰지 않고 따로 동작한다. 
따라서 작업이 순차적으로 진행되지 않는다.

## 블로킹과 동기는 어떤 차이인가?
두 개념은 유사하면서도 차이가 있다.

✅ 동기(Synchronous):
- 호출한 함수가 호출된 함수의 결과를 반드시 기다린다.
- 작업이 순차적으로 진행된다.
- '기다림'이 반드시 스레드의 멈춤(블로킹)을 의미하지는 않는다.

✅ 블로킹(Block):
- 호출한 함수(스레드)가 결과를 기다리는 동안 아무 작업도 하지 못하고 멈추는 상태
- 스레드가 대기 상태로 남아 자원을 점유한다.

✅ 정리:
- 동기 ≠ 반드시 블로킹
- 비동기 ≠ 반드시 논블로킹
- 예시: 비동기 블로킹 I/O, 동기 논블로킹 I/O 모두 가능하다.

## 스프링에서 비동기 처리는 어떻게 하며 무엇을 주의해야 하는가?
스프링에서는 ```@Async``` 어노테이션을 사용하여 비동기 처리를 수행할 수 있다.
해당 어노테이션을 사용하기 위해서는 몇 가지 주의 점이 있다.
- 기본적으로 ```@Async```가 적용된 메서드에서 발생하는 예외는 호출자에게 전파되지 않는다.
- 비동기 메서드에서 예외를 정상적으로 처리하기 위해서는 별도의 비동기 예외 처리기를 사용해야한다.
- 또한, ```@Async``` 어노테이션은 프록시 기반으로 동작하기 때문에 같은 클래스 내부에서 직접 호출하는 경우 별도의 스레드에서 메서드가 실행되지 않는다.
- 비동기 메서드 내에서 생성한 트랜잭션은 상위 트랜잭션과 무관한 생명주기를 가진다.

- 기본적으로 ```@Async``` 어노테이션이 적용된 메서드는 별도의 스레드 풀에서 실행된다.
- ```@EnableAsync``` 어노테이션을 설정 클래스에 추가해야 ```@Async```가 활성화된다.
- 반환 타입은 보통 ```void```, ```Future```, ```CompletableFuture```를 사용한다.

✅ 비동기 예외 처리:
- 비동기 메서드의 예외는 호출자에게 전파되지 않으므로 ```AsyncUncaughtExceptionHandler```를 구현하여 예외를 처리한다.

✅ 프록시 기반 주의사항:
- 같은 클래스 내부에서 호출 시 프록시가 적용되지 않아 비동기로 동작하지 않는다.
- 반드시 외부에서 호출되어야 한다.

✅ 트랜잭션 주의:
- 비동기 메서드 내의 트랜잭션은 별도의 독립된 트랜잭션으로 처리된다.
- 예상과 다르게 롤백이 적용되지 않을 수 있다.

✅ 알고 가면 좋은 내용:
- 비동기 처리는 CPU 바운드 작업보다는 I/O 바운드 작업(네트워크 호출, 파일 처리 등)에 적합하다.
- 과도한 비동기 사용은 오히려 스레드 풀 고갈 및 시스템 부하로 이어질 수 있다.
- Reactor, CompletableFuture와의 차이점도 알아두면 좋다.


---
# 예제 코드
## 비동기 설정 클래스
```java
@Configuration // 설정 클래스임을 나타냄 (Spring Bean으로 등록)
@EnableAsync   // 비동기 처리 기능 활성화
public class AsyncConfig {

    @Bean(name = "asyncTaskExecutor") // 스레드 풀을 Spring Bean으로 등록
    public Executor asyncTaskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();

        // 기본 스레드 수 (핵심 풀 크기) → 최소 스레드 개수
        executor.setCorePoolSize(5);

        // 최대 스레드 수 → 요청량이 많을 때 최대 몇 개까지 늘어날지
        executor.setMaxPoolSize(10);

        // 큐에 대기할 수 있는 최대 요청 수
        executor.setQueueCapacity(100);

        // 스레드 이름 접두어 → 디버깅/모니터링에 유용
        executor.setThreadNamePrefix("AsyncExecutor-");

        executor.initialize();
        return executor;
    }
}
```
> 👉 이 설정을 하면 @Async("asyncTaskExecutor") 에서 사용할 스레드 풀이 생성된다.
## 비동기 서비스 
```java
@Service // Spring이 관리하는 서비스 빈
public class NotificationService {

    @Async("asyncTaskExecutor") // 비동기 실행을 지정 → 별도의 스레드 풀에서 실행
    public CompletableFuture<String> sendNotification(String message) {
        try {
            // 시간 지연 시뮬레이션 (예: 외부 시스템 호출)
            Thread.sleep(3000);
            System.out.println("알림 전송 완료: " + message);
        } catch (InterruptedException e) {
            // 예외 발생 시 Unchecked Exception으로 감싸서 던짐
            throw new IllegalStateException("알림 전송 실패", e);
        }

        // 비동기 결과 반환 (즉시 완료 상태로)
        return CompletableFuture.completedFuture("완료");
    }

    @Async("asyncTaskExecutor") // 비동기 결과를 활용하는 버전
    public CompletableFuture<String> sendNotificationWithResult(String message) {
        try {
            Thread.sleep(3000); // 예: 외부 API 호출
            System.out.println("알림 전송 완료: " + message);
            return CompletableFuture.completedFuture("알림 전송 성공");
        } catch (InterruptedException e) {
            throw new IllegalStateException("알림 전송 실패", e);
        }
    }
}
```
>	•	@Async 덕분에 별도의 스레드에서 실행 → 호출자는 대기하지 않음
>	•	CompletableFuture → 비동기 작업 결과를 반환하는 컨테이너

## 호출 컨트롤러
```java
@RestController // REST API 컨트롤러임을 명시
public class NotificationController {

    private final NotificationService notificationService;

    // 생성자 주입
    public NotificationController(NotificationService notificationService) {
        this.notificationService = notificationService;
    }

    @GetMapping("/send") // GET 요청 처리
    public String send() {
        // 비동기 호출: 결과 기다리지 않고 바로 다음 줄 실행
        notificationService.sendNotification("새 알림");

        // 클라이언트에는 즉시 응답 → 비동기 작업은 백그라운드에서 진행
        return "요청 완료 (알림 전송 중)";
    }

    @GetMapping("/send-with-result") // 비동기 결과를 활용하는 버전
    public CompletableFuture<String> sendWithResult() {
        // 비동기 결과를 그대로 반환
        return notificationService.sendNotificationWithResult("새 알림");
    }
}
```
> 호출자는 sendNotification() 결과를 기다리지 않기 때문에 즉시 응답 가능하다.

> 비동기 결과를 활용하는 경우 바로 return을 해주면 Spring MVC가 응답을 위임 받아 비동기 처리 완료후 자동으로 응답을 생성해준다. 

> 즉, CompletableFuture<String>이 반환한 값이 HTTP 응답의 Body가 된다.

### 비동기 결과를 활용하면 리턴되는 결과
``` http
HTTP/1.1 200 OK
Content-Type: text/plain;charset=UTF-8

알림 전송 성공
```

## 비동기 예외 처리 설정
```java
@Configuration
public class AsyncExceptionConfig implements AsyncConfigurer {

    @Override
    public Executor getAsyncExecutor() {
        // 간단한 Executor (예제용)
        return new SimpleAsyncTaskExecutor();
    }

    @Override
    public AsyncUncaughtExceptionHandler getAsyncUncaughtExceptionHandler() {
        // 비동기 예외 처리 (호출자에게 전달되지 않음 → 반드시 처리 필요)
        return (ex, method, params) -> {
            System.out.println("비동기 예외 발생: " + ex.getMessage());
        };
    }
}
```
> 비동기 메서드의 예외가 호출자에게 도달하지 않기 때문에 별도로 이렇게 설정해줘야 로그라도 남는다.

### 흐름 요약
```txt
✅ 현재 페이지의 예제 흐름 요약
1.	클라이언트 → /send API 호출
2.	NotificationController.send() 호출됨
3.	notificationService.sendNotification("새 알림") 호출
4.	→ @Async 덕분에 별도의 스레드에서 실행 시작 (비동기)
5.	컨트롤러는 결과 기다리지 않고 바로 “요청 완료 (알림 전송 중)” 응답 반환
6.	별도의 스레드에서는 Thread.sleep(3000) → 3초 후 알림 전송 완료: 새 알림 출력
7.	마지막으로 CompletableFuture.completedFuture("완료") 반환 (하지만 컨트롤러에서는 사용 안 함)
```

### 예상 결과
```txt
요청 완료 (알림 전송 중)
(3초 뒤)
알림 전송 완료: 새 알림
```