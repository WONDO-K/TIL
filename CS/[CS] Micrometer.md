# Micrometer
## Micrometer란?
- 벤더 중립적인 메트릭 계측 라이브러리로, 애플리케이션에서 발생하는 다양한 지표(예: CPU 사용량, 메모리 소비, HTTP 요청 및 커스텀 이벤트)를 수집한다.
- Prometheus, Datadog, Graphite 등 여러 모니터링 시스템에 메트릭을 전송할 수 잇도록 단순하고 일관된 API(파사드)를 제공하여, 각 백엔드 클라리언트의 복잡한 세부 구현을 감춘다.
- 특히, Spring Boot Actuator와 깊이 통합되어, 기본 메트릭을 자동으로 수집하고 노출할 수 있다.

## Micrometer와 Spring Boot Actuator의 관계
- Spring Boot Actuator는 애플리케이션의 상태, 환경, 로그 등 여러 운영 정보를 노출하는 관리 엔드포인트를 제공한다.
- 내부적으로 Actuator는 Micrometer를 사용하여 JVM, HTTP, 데이터베이스 등 다양한 메트릭을 수집한다.
- 즉 Actuator는 모니터링 및 관리 인터페이스를 제공하고, Micrometer는 그 밑에서 실제 메트릭 데이터를 계측하고 여러 모니터링 시스템으로 전송하는 역할을 담당한다.

```java
package com.example.metrics;

import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.Gauge;
import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Timer;
import org.springframework.stereotype.Service;

@Service
public class CustomMetricsService {

    private final Counter requestCounter;
    private final Timer requestTimer;
    private final CustomGauge customGauge;

    // 생성자에서 MeterRegistry를 주입받아 필요한 메트릭을 등록합니다.
    public CustomMetricsService(MeterRegistry meterRegistry) {
        // HTTP 요청 총 건수를 세는 Counter (태그로 엔드포인트 구분)
        this.requestCounter = meterRegistry.counter("custom.requests.total", "endpoint", "/api/test");

        // HTTP 요청 처리 시간을 측정하는 Timer (태그로 엔드포인트 구분)
        this.requestTimer = meterRegistry.timer("custom.request.duration", "endpoint", "/api/test");

        // Gauge: 예를 들어, 현재 활성 세션 수를 측정하기 위한 커스텀 객체를 등록
        this.customGauge = new CustomGauge();
        Gauge.builder("custom.active.sessions", customGauge, CustomGauge::getActiveSessions)
                .tag("region", "us-east")
                .register(meterRegistry);
    }

    /**
     * 실제 비즈니스 로직을 실행할 때 요청 카운트와 처리 시간을 측정합니다.
     * @param requestLogic 실제 처리할 로직 (예: HTTP 요청 처리)
     */
    public void processRequest(Runnable requestLogic) {
        // 요청 수 증가
        requestCounter.increment();
        // 요청 처리 시간 측정
        requestTimer.record(requestLogic);
    }

    /**
     * 활성 세션 수 업데이트 (예를 들어, 로그인/로그아웃 이벤트에서 호출)
     * @param activeSessions 현재 활성 세션 수
     */
    public void updateActiveSessions(int activeSessions) {
        customGauge.setActiveSessions(activeSessions);
    }

    /**
     * 커스텀 Gauge의 값을 저장하는 내부 클래스.
     */
    private static class CustomGauge {
        // 현재 활성 세션 수를 저장 (volatile을 사용해 스레드 안정성 확보)
        private volatile double activeSessions = 0;

        public double getActiveSessions() {
            return activeSessions;
        }

        public void setActiveSessions(double activeSessions) {
            this.activeSessions = activeSessions;
        }
    }
}
```
- MeterRegistry
    - 생성자에서 MeterRegistry를 주입받아 애플리케이션의 모든 메트릭을 중앙에서 관리하고, 설정ㄷ된 모니터링 백엔드를 주기적으로 전송한다.
- Counter
    - requestCounter는 /api/test 엔드 포인트에 대한 요청 건수를 카운트한다.
    - 매 HTTP 요청마다 increment() 호출로 증가시킨다.
- Timer 
    - requestTimer는 HTTP 요청 처리 시간을 측정한다.
    - record() 메서드를 사용해 실제 로직 실행 시간을 기록한다.
- Gauge
    - customGauge는 현재 활성 세션 수를 측정하는 데 사용된다.
    - 항상 현재 상태를 조회하는 함수(getActivateSessions()를 호출하여 실시간 값을 반영한다.
- Volatile
    - 멀티 스레드에서 변수 값 동기화 문제 해결을 위한 키워드
    - 여러 스레드가 동시에 같은 변수에 접근할 때 CPU 캐시와 메인 메모리 간의 비동기 문제가 발생할 수 있다.
```java
class SharedResource {
    static boolean flag = false; // 공유 변수
}

public class VolatileExample {
    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> {
            while (!SharedResource.flag) { // flag 값이 false이면 계속 루프
            }
            System.out.println("Thread 1 종료됨!");
        });

        Thread thread2 = new Thread(() -> {
            try { Thread.sleep(1000); } catch (InterruptedException e) {}
            SharedResource.flag = true; // 1초 후 flag 값을 true로 변경
            System.out.println("Thread 2: flag 값을 변경!");
        });

        thread1.start();
        thread2.start();
    }
}
-->

class SharedResource {
    static volatile boolean flag = false; // 🔥 volatile 추가
}

```
- thread2가 flag = true;로 변경해도 CPU 캐시에 저장되어 다른 스레드에는 반영되지 않을 수도 있음.
- volatile를 사용하면 flag 값이 변경되면 즉시 메인 메모리에 반영되므로, 모든 스레드에서 변경 사항을 즉시 감지 가능
- 핵심 기능
    - 메인 메모리에서 직접 읽고 씀(CPU 캐시를 안 씀)
    - 재정렬 방지 (JVM이 실행 순서를 최적화하는 과정에서 순서가 바뀌는 것을 방지)
    - 다만 i++ 같은 복합 연산은 원자성을 보장하지 못한다 -> 동기화 필요
        - i++는 읽기 → 증가 → 쓰기 3단계 연산이므로, 여러 스레드가 동시에 접근하면 데이터가 덮어써질 가능성이 있음.