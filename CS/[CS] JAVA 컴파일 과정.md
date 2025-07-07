# Java의 컴파일 과정
## Java는 컴파일 언어이면서 인터프리터 언어의 특징을 함께 갖는다.
1. 작성 (Write)
- 개발자가 .java 확장자를 가진 소스코드를 작성
2. 컴파일(Compile)
- javac 명령어로 Java 컴파일러가 소스코드를 바이트코드(class)로 변환한다.
- 이 과정에서 문법 오류가 검출된다. (컴파일 오류)
3. 클래스 로드(Load)
- 클래스 로더(ClassLoader)가 .class 파일을 JVM의 메모리에 올린다.
- 여러 개의 .class 파일을 필요한 시점에 동적으로 로드한다.
4. 바이트 코드 검증(Verify)
- JVM의 바이트코드 검증기가 클래스의 안정성을 검증한다.
- 잘못된 코드, 해킹 시도등을 방지
5. 실행(Interpret & Complie)
- JVM의 인터프리터가 바이트코드를 한 줄씩 읽어 실행하거나
- JIT(Just-In-Time)컴파일러가 자주 호출되는 코드(HotSpot)를 기계어로 변환하여 성능을 높인다.
6. 실행
- 최종적으로 OS 위에서 네이티브 코드로 실행된다.


## 도식화
[1] 소스코드 작성
   ↓
Hello.java
(개발자가 작성)

[2] 컴파일 (javac)
   ↓
Hello.class
(바이트코드 생성)

[3] 클래스 로딩 (ClassLoader)
   ↓
JVM 메모리 (Method Area에 로드)

[4] 바이트코드 검증 (Bytecode Verifier)
   ↓
안전성 검사

[5] 실행 (Interpreter & JIT Compiler)
   ↓
HotSpot 최적화 (자주 쓰는 코드 → 기계어)

[6] 네이티브 코드 실행 (OS 위에서 동작)

## 실무 예시: Spring Boot 서비스 실행
1.	./gradlew build → build/libs/app.jar 생성 (.class 포함)
2.	서버에 app.jar 배포
3.	java -jar app.jar → JVM 실행 → 클래스 로드 → 서비스 시작
4.	자주 호출되는 API 메서드 → JIT 컴파일 → 성능 최적화

✅ 이 흐름은 클라우드 서버/도커 컨테이너 어디서든 동일하게 적용된다.

|질문포인트| 답변|
|-|-|
|JIT이란?|자주 호출되는 메서드를 네이티브 코드로 변환해 성능 향상|
|인터프리터 vs JIT?|인터프리터: 한 줄씩 실행 / JIT: HotSpot 최적화|
|JVM의 역할?|메모리 관리, GC, 바이트코드 실행, 플랫폼 독립성 제공|
|JVM 메모리 구조?|Heap, Stack, Method Area, PC Register|
