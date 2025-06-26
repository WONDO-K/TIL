# Checked Exception과 Unchecked Exception
## Checked Exception
컴파일 시점에 확인되며, 반드시 처리해야 하는 예외이다. 자바에서는 IOException, SQLException 등이 이에 속한다. 
Checked Exception을 유발하는 메서드를 호출하는 경우, 메서드 시그니처에 throws를 사용하여 호출자에게 예외를 위임하거나 
메서드 내에서 try-catch를 사용하여 해당 예외를 반드시 처리해야 한다.

## Unchecked Exception
런타임 시점에 발생하는 예외로, 컴파일러가 처리 여부를 강제하지 않는다. 자바에서는 RuntimeException을 상속한 예외들이 해당된다.
일반적으로 프로그래머의 실수나 코드 오류로 발생한다.

## 각각 언제 사용해야 하는가?
### Checked Exception
Checked Exception은 외부 환경과의 상호작용에서 발생할 가능성이 높은 예외에 적합하다.
예를 들어, 파일 입출력, 네트워크 통신 등에서 발생할 수 있는 예외는 Checked Exception으로 처리하는 것이 좋다.
이러한 예외는 예측 가능하며, 호출하는 쪽에서 적절히 처리할 수 있는 여지가 있다.
### Unchecked Exception
코드 오류, 논리적 결함 등 프로그래머의 실수로 인해 발생할 수 있는 예외에 적합하다.
예를 들어, null 참조 또는 잘못된 인덱스 접근 등은 호출자가 미리 예측하거나 처리할 수 없기 떄문에 Unchecked Exception으로 두는 것이 좋다.

## Error와 Exception의 차이
### Error
주로 JVM에서 발생하는 심각한 문제로, ```OutOfMemoryError, StackOverflowError``` 등 시스템 레벨에서 발생하는 오류이다.
이는 일반적으로 프로그램에서 처리하지 않으며, 회복이 어려운 오류에 속하며, 애플리ㅔ이션 코드에서 복구할 수 없는 심각한 문제를 나타낸다.
### Exception
프로그램 실행 중 발생할 수 있는 오류 상황을 나타낸다. 대부분의 경우 회복 가능성이 있으며, 프로그램 내에서 예외 처리를 통해 오류 상황을 제어할 수 있다.
Exception은 ``` checked Exception, Unchecked Exception ``` 으로 나눌 수 있다.

---

## ✅ 보충 설명 및 추가적으로 알면 좋은 내용

### 1. 예외 계층 구조 정리
Java의 예외는 `Throwable` 클래스를 루트로 가지며, 두 가지 주요 하위 클래스가 존재한다:
```
Throwable
├── Error              (ex. OutOfMemoryError, StackOverflowError)
└── Exception
    ├── Checked Exception  (ex. IOException, SQLException)
    └── Unchecked Exception (ex. NullPointerException, IllegalArgumentException)
```
면접에서는 "Java 예외의 계층 구조를 설명해보세요"라는 질문이 자주 등장할 수 있다.

### 2. Checked vs Unchecked의 설계 철학
- Checked Exception은 "회복 가능한 예외"를 호출자에게 강제로 인지시키는 목적이 있다.
  → 컴파일 타임에 처리 강제 → 안정성 증가
- Unchecked Exception은 프로그램의 논리적 오류나 버그의 가능성이 높은 예외다.
  → 로직 자체를 수정해야 함 → 예외 처리보다 설계 개선이 핵심이다.

실무에서는 RuntimeException을 선호하는 경향이 있다. 
Checked Exception의 남용은 코드의 가독성을 해치고, 불필요한 try-catch 또는 throws 선언을 남발하게 만들기 때문이다.

❗️여기서 말하는 "가독성을 해친다"는 의미는 단순히 코드가 길고 읽기 힘들다는 뜻이 아니다.
진짜 문제는 "명시성의 과잉 또는 부족"에서 온다.
예를 들어, checked Exception을 사용하는 경우, 메서드 시그니처에 'throws'가 계속 확산되며 코드 흐름을 따라가기 어렵고,
이로 인해 실제 로직보다 예외 전달에 더 많은 신경을 쓰게 된다. 결과적으로 코드의 목적이 흐려지고, 가독성이 떨어진다.

#### 'throws'가 계속 확산된다는 말이 뭔가?
예외 위임이 발생한다는 의미로 어떤 메서드에서 발생할 수 있는 Checked Exception을 try-catch로 직접 처리하지 않고,
그 예외를 호출한 메서드에게 “떠넘기는” 것을 의미한다.

> 즉, “난 이 예외를 여기서 처리 안 할래, 위에서 처리해줘”
라고 하는 것이 thorws

🔸 예시: 위임이 계속 누적될 때
```java
public void controller() throws IOException {
    service(); // 여기서 처리 안 하고 위로 위임
}

public void service() throws IOException {
    repository(); // 여기서도 처리 안 함
}

public void repository() throws IOException {
    new FileReader("data.txt"); // 여기서 실제 IOException 발생 가능
}
```
•	repository()에서 발생 가능한 IOException을 처리하지 않고 throws IOException
•	그걸 service()가 받아서 또 throws IOException
•	마지막에 controller()도 throws IOException → 결국 예외가 계속 “위로” 전달

### 3. 사용자 정의 예외(Custom Exception)
비즈니스 로직에 맞춘 커스텀 예외 정의가 필요할 수 있다:
```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String message) {
        super(message);
    }
}
```
주로 RuntimeException을 상속하여 사용하며, 응용 서비스 레이어에서 로직 흐름 제어에 활용된다.

### 4. 예외 처리 vs 회복 전략
예외를 단순히 try-catch로 감싸는 것이 아닌, "복구 전략"을 어떻게 설계할 것인지가 중요하다.
예: 파일 읽기 실패 시 다른 경로로 시도, 네트워크 실패 시 재시도 로직 등

### 5. 예외 전환(Exception Wrapping)
Checked → Unchecked로 전환해 도메인 로직에서 사용하기 쉽게 만든다:
```java
try {
    // IO 처리
} catch (IOException e) {
    throw new RuntimeException("파일 처리 실패", e);
}
```
예외 정보를 숨기지 말고 감싸서 전달하는 것이 좋은 패턴이다.

### 💬 면접에서는 이렇게 나올 수 있어요
> ❓ "RuntimeException을 사용하면 예외 처리를 안 해도 되는데, 무조건 RuntimeException으로 쓰는 게 좋은 거 아닌가요?"
>
> ✅ 답변 예시:
> "RuntimeException은 로직 오류를 표현하는 데 적합하지만, 회복 가능한 외부 오류는 Checked Exception으로 강제해야 사용자에게 책임을 넘길 수 있습니다. 다만 실무에서는 불필요한 예외 전파를 피하기 위해 RuntimeException을 더 선호하며, 예외는 일관성 있게 설계하는 것이 더 중요합니다."

✅ 핵심 개념

예외 전환이란?
	•	Checked Exception을 받아서 Unchecked Exception(보통 RuntimeException)으로 감싸서 던지는 것
	•	목적: 호출자에게 처리 강제를 피하면서도 예외의 원인을 숨기지 않고 전달

```java
try {
    // IO 처리
} catch (IOException e) {
    throw new RuntimeException("파일 처리 실패", e);
}
```
의미 분석:
	•	IOException은 Checked Exception → 호출자에게 throws나 try-catch를 강제
	•	하지만 이걸 RuntimeException으로 감싸서 다시 던지면:
	•	더 이상 throws 선언도 필요 없음
	•	도메인 로직에서는 예외 흐름을 더 단순하게 관리 가능
	•	e를 두 번째 인자로 넘겨 원래 예외 스택 트레이스를 보존

🛠 실무에서의 활용 예
```java
public String readFile(String path) {
    try {
        return Files.readString(Path.of(path));
    } catch (IOException e) {
        throw new FileReadFailedException("파일 읽기 실패: " + path, e);
    }
}
```
→ FileReadFailedException은 RuntimeException을 상속한 커스텀 예외
→ 비즈니스 로직에서는 더 이상 IOException에 신경 쓸 필요 없이
→ FileReadFailedException만 catch하거나, 전파할 수 있음

❗️왜 이렇게 쓰는가?
- Checked Exception 남발 방지
- 서비스/도메인 레이어에서 로직 흐름 깔끔하게 유지
- 예외 발생 시 로그와 원인(스택 트레이스)을 보존하면서도, 예외 처리 부담을 필요한 곳에만 집중

### 💬 면접에서는 이렇게 나올 수 있어요
❓ “왜 Checked Exception을 굳이 RuntimeException으로 감싸나요?”

✅ 답변 예시:
“Checked Exception을 그대로 전파하면 호출자마다 try-catch나 throws 처리가 반복돼 가독성이 떨어집니다. 
그래서 예외를 RuntimeException으로 감싸서 도메인 로직을 간결하게 만들고, 필요할 때만 처리하도록 설계합니다. 
단, 원래 예외는 함께 넘겨서 로그나 디버깅 정보를 보존하는 것이 중요합니다.”

✅ 실무에서는 이렇게 균형 맞춤
	•	외부 리소스 등 회복 가능성이 있는 예외는 Checked로 명확히 알림
	•	도메인 로직 내에서는 RuntimeException 또는 커스텀 Unchecked 예외로 통일해서 로직 흐름을 명확히 유지
	•	예외 wrapping 시 메시지 + 원인 포함해서 디버깅 가능성 확보