# 싱글톤 패턴
생성자를 여러차례 호출해도 실제로 생성되는 객체는 하나로 유지하는 것을 의미한다.
객체가 최초로 생성된 이후에 생성자나 객체 생성 메서드는 기존에 만들어진 객체를 반환한다.

```java
public class Singleton {

  private static final Singleton INSTANCE = new Singleton();

  // 생성자 호출 제한
  private Singleton() { ... }

  public static Singleton getInstance() {
    return INSTANCE;
  }
}
```
- static : 클래스가 메모리에 로딩될 때 단 한 번 초기화됨
- final : 이후 재할당이 불가능해짐 -> 인스턴스 불변 상태로 강제함
- private singleton() 생성자 : 외부에서 new Singleton() 불가
## 해당 코드 동작 흐름
1. Singleton 클래스가 처음 로딩될 때 static에 의해 INSTANCE가 메모리에 딱 한번만 new Singleton()으로 초기화된다.
2. 이후 getInstance() 호출될 때 마다 INSTANCE를 리턴한다.
return INSTANCE를; -> 이 부분에서 이미 만들어진 INSTANCE를 반환하는 것
new Singleton()은 오직 클래스 로딩 시 INSATANCE 필드에서만 한 번 실행된다.
그 외에는 INSTANCE라는 메모리 주소를 계속 참조하는 것

## 싱글톤의 장단점
### 장점
하나의 객체를 여러 상황에서 재사용이 가능하기 떄문에 메모리 낭비를 방지할 수 있다.
또한, 여러 다른 객체가 하나의 인스턴스에 쉽게 접근 가능하여 편리하다.
### 단점
- 싱글턴은 전역 객체를 생성한다는 특성상 코드의 복잡도를 높이고 테스트하기 어려운 코드를 만들 수 있다는 단점이 있다.
- 상황에 따라 더욱 복잡한 구현이 필요할 수도 있다.
    - 예를 들어, 싱글턴 객체를 지연 초기화(Lazy initialization)하고 싶을 때 여러 스레드가 동시에 생성자에 접근하면 두개 이상의 객체가 생성될 수 있으므로 동시성 문제를 고려해야한다.
- 테스트에서는 싱글탠 객체의 상태를 초기화하는 과정이 필요하다. 예를 들어, 1번 테스트에서 싱글턴 객체를 수정한 경우, 2번 테스트는 싱글턴의 상태를 초기화한 후 테스트를 실행해야 한다.
- 싱글턴 객체가 인터페이스를 구현하지 않은 경우 테스트 환경에서 가짜 구현체로 대체하여 주입하기가 어렵다.

#### 예시와 설명

1. **멀티스레드 환경에서 동시성 문제 (지연 초기화 시)**  
   아래처럼 Lazy Initialization으로 싱글톤을 구현하면, 두 개의 스레드가 동시에 `getInstance()`를 호출할 경우 **두 번 생성자 호출**이 발생할 수 있습니다.

   ```java
   public class LazySingleton {
       private static LazySingleton instance;

       private LazySingleton() {}

       public static LazySingleton getInstance() {
           if (instance == null) {
               instance = new LazySingleton(); // 동시 접근 시 문제 발생 가능
           }
           return instance;
       }
   }
   ```

   → 해결 방법: `synchronized` 키워드로 동기화하거나, double-checked locking 사용 필요

    → 예시: 멀티스레드에서 실제 문제가 발생하는 상황

    아래 코드는 두 개의 스레드가 동시에 `getInstance()`를 호출할 경우, 서로 다른 인스턴스를 생성해 싱글톤이 깨지는 상황을 보여줍니다.

    ```java
    public class LazySingleton {
        private static LazySingleton instance;

        private LazySingleton() {
            System.out.println("생성자 호출됨 by " + Thread.currentThread().getName());
        }

        public static LazySingleton getInstance() {
            if (instance == null) {
                try {
                    Thread.sleep(100); // 일부러 지연
                } catch (InterruptedException ignored) {}
                instance = new LazySingleton();
            }
            return instance;
        }
    }
    ```

    ```java
    public class Main {
        public static void main(String[] args) {
            Runnable task = () -> {
                LazySingleton instance = LazySingleton.getInstance();
                System.out.println(instance);
            };

            Thread t1 = new Thread(task);
            Thread t2 = new Thread(task);

            t1.start();
            t2.start();
        }
    }
    ```

    ### 실행 결과 예시 (상황에 따라 다름)
    ```
    생성자 호출됨 by Thread-0
    생성자 호출됨 by Thread-1
    LazySingleton@1a2b3c
    LazySingleton@4d5e6f
    ```

    → 서로 다른 인스턴스가 생성되어 싱글톤 패턴이 깨짐

2. **테스트 간 상태 공유로 인한 부작용**
   ```java
   public class AppConfig {
       private static final AppConfig INSTANCE = new AppConfig();
       private String mode = "default";

       private AppConfig() {}

       public static AppConfig getInstance() {
           return INSTANCE;
       }

       public void setMode(String mode) {
           this.mode = mode;
       }

       public String getMode() {
           return mode;
       }
   }
   ```

   ```java
   // 테스트 A
   @Test
   void testSetModeToDev() {
       AppConfig.getInstance().setMode("dev");
   }

   // 테스트 B
   @Test
   void testModeShouldBeDefault() {
       assertEquals("default", AppConfig.getInstance().getMode()); // 실패 가능
   }
   ```

   → 테스트 간 상태 격리가 어려워져 예측 불가능한 실패 발생 가능

3. **인터페이스 미구현으로 인해 대체 불가**

   ```java
   public class NotificationService {
       public void send(String msg) {
           // 실제 발송 로직
       }
   }

   public class UserService {
       private final NotificationService notificationService = NotificationService.getInstance();

       public void notifyUser(String msg) {
           notificationService.send(msg);
       }
   }
   ```

   → 테스트 시 `NotificationService`를 목으로 바꾸고 싶어도 인터페이스로 추상화돼 있지 않으면 주입이 어렵고, DI 환경에 적합하지 않음

---

## ✅ 멀티스레드 실전 예제 및 사용 상황

### 1. 직접 `Thread`, `Runnable`을 사용하는 기본 예제

```java
public class MyTask implements Runnable {
    @Override
    public void run() {
        System.out.println("작업 실행: " + Thread.currentThread().getName());
    }

    public static void main(String[] args) {
        Thread t1 = new Thread(new MyTask());
        Thread t2 = new Thread(new MyTask());

        t1.start();
        t2.start();
    }
}
```

### 2. 실무에서 자주 쓰는 `ExecutorService` 방식

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 0; i < 5; i++) {
            final int taskId = i;
            executor.submit(() -> {
                System.out.println("작업 " + taskId + " 시작 - " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // 시간 소요 작업
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("작업 " + taskId + " 종료 - " + Thread.currentThread().getName());
            });
        }

        executor.shutdown();
    }
}
```

---

## ✅ 실수로 발생할 수 있는 멀티스레드 문제: Race Condition

```java
public class Counter {
    private int count = 0;

    public void increment() {
        count++; // 문제 발생 가능
    }

    public int getCount() {
        return count;
    }

    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();

        Runnable task = () -> {
            for (int i = 0; i < 10000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println("최종 카운트 값: " + counter.getCount()); // 20000이 아닐 수 있음
    }
}
```

→ `count++`는 비원자적 연산이기 때문에 두 스레드가 동시에 접근하면 덮어쓰기 발생 가능  
→ 해결 방법: `synchronized`, `AtomicInteger`, `ReentrantLock` 사용