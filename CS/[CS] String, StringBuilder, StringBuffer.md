# String, StringBuilder, StringBuffer의 차이

---

## 📌 String, StringBuilder, StringBuffer 차이 (기초 개념부터)

### 1. String (불변 객체, Immutable)
- 한 번 생성된 문자열은 **절대 변경 불가**하다.
- 문자열을 변경하는 것처럼 보여도 항상 **새로운 String 객체**가 생성된다.

```java
String str = "hello";
str += " world";  // 실제로는 새로운 String 객체가 만들어짐
```

✅ 장점: 
- 쓰레드 안전성
- 간단하고 직관적

❗ 단점: 
- 문자열 변경이 잦을 경우 성능 저하 → GC 부담

---

### 2. StringBuilder (가변 객체, Mutable) ✏️
- 문자열을 **변경 가능한 객체**로 다룬다.
- 문자열 연결 시에도 **새 객체 생성 없이** 기존 객체를 재사용한다.

```java
StringBuilder sb = new StringBuilder("hello");
sb.append(" world");
System.out.println(sb.toString());  // hello world
```

✅ 장점:
- 성능 우수 (특히 반복적인 문자열 변경 시)

❗ 단점:
- **쓰레드 안전성 보장 X**

---

### 3. StringBuffer (멀티쓰레드 환경 대응) 🔒
- StringBuilder와 거의 동일하나, **멀티쓰레드 환경**에서도 안전하도록 **동기화(synchronized)** 되어 있다.

```java
StringBuffer sbf = new StringBuffer("hello");
sbf.append(" world");
System.out.println(sbf.toString());  // hello world
```

✅ 장점:
- 멀티쓰레드에서 안전성이 있다

❗ 단점:
- 성능은 StringBuilder보다 다소 낮음

---

## 📝 언제 어떤 걸 쓰나요?

| 상황 | 추천 클래스 |
|------|------------|
| 문자열 변경 거의 없음 | `String` |
| 문자열 변경 多, 단일쓰레드 | `StringBuilder` |
| 문자열 변경 多, 멀티쓰레드 | `StringBuffer` |

---

## 💡 면접에서는 이렇게 질문 나올 수 있어요 (알고리즘 문제 풀이 예시 포함)

1. **“StringBuilder와 StringBuffer 차이점은?”**  
→ 둘 다 **가변 문자열 클래스**지만,  
StringBuffer는 **멀티쓰레드 환경**에서 동기화를 제공하여 **스레드 안전성이 있다**.  
반면 StringBuilder는 **단일 스레드 환경**에서 성능이 더 우수하다.  

📌 **예시:**  
- **단일 스레드 알고리즘**(예: LeetCode, 백준)에서는 **StringBuilder** 사용 → 빠른 성능  
- **멀티스레드 환경**에서 문자열 조작 필요 → **StringBuffer** 사용

2. **“String은 왜 불변인가요?”**  
→ 한 번 만들어진 문자열은 **변경되지 않는 immutable 객체**다.  
그 이유는:
- **해시코드 캐싱** (HashMap key로 안전 사용)
- **보안성** (URL, 환경변수 등 안전 보장)
- **스레드 안전성** (공유해도 상태 변하지 않음)

📌 **예시:**  
- 알고리즘 문제 풀이에서 String의 **substring()**, **charAt()** 등을 호출해도  
원본 문자열은 변하지 않음 → 복잡한 코드 없이 안정적으로 재사용 가능

3. **“자바에서 문자열 성능 최적화 방법은?”**  
→ 반복적인 문자열 연결이 많은 경우:
- `StringBuilder` 사용 (알고리즘에서 매우 자주 사용)
- `StringBuffer` 사용 (멀티스레드 필요시)
- `String.format` 대신 `Formatter` 또는 `StringBuilder` 사용

📌 **예시:**  
```java
// 알고리즘 문제에서 StringBuilder 사용 (백준, 프로그래머스 등)
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i).append(" ");
}
System.out.println(sb.toString());
```
- 위와 같은 문제를 `String`으로 풀면 매번 새로운 객체 생성 → 시간초과, 메모리 초과 발생 가능

---

## 🔑 핵심 요약 (보완)

| 용어 | 의미 |
|------|------|
| **동기화 (Synchronization)** | 여러 스레드가 동시에 같은 자원에 접근하는 것을 막아 데이터 충돌을 방지하는 기술 |
| **스레드 안전성 (Thread Safety)** | 여러 스레드가 동시에 접근해도 데이터 일관성과 무결성이 유지되는 상태 |
| **StringBuffer** | 동기화 O → 멀티스레드 환경에서 안전성 보장, 성능 다소 저하 |
| **StringBuilder** | 동기화 X → 단일 스레드 환경에서 빠름 |

---

## 🔑 동기화(Synchronization)란? (보완)

📌 한 줄 정의:
- **“여러 스레드가 동시에 공유 자원에 접근하지 못하도록 차례대로 접근하게 하는 기술”**이다.

❓ 왜 ‘막는다’는 표현인데 ‘동기화’라고 부를까?
- 여기서 **“동기화”**란 서로 다른 스레드들이 “순서를 맞춰서” 자원에 접근하도록 만든다는 뜻이다.
- 즉, 동시에 들어오면 경쟁(Race Condition)이 발생하기 때문에 **‘내가 쓰고 있을 땐 너는 기다려’**라고 하는 것이다.
- ‘한 번에 하나씩, 차례차례’ → 이걸 synchronize (동기화) 라고 부른다.

✅ 스레드 안전(Thread Safety)과의 관계:
- 동기화는 스레드 안전성을 확보하는 한 가지 방법이다.
- 동기화가 잘 되어 있다면 여러 스레드가 동시에 접근하더라도 데이터 일관성과 무결성이 유지된다.

✅ StringBuffer vs StringBuilder와의 연결:
| 클래스 | 동기화 | 스레드 안전성 | 성능 |
|--------|--------|---------------|------|
| StringBuffer | O | O | 다소 느림 |
| StringBuilder | X | X (단일 스레드만 안전) | 빠름 |

💡 정리:
- **멀티스레드 환경:** StringBuffer (동기화 필요)
- **단일스레드 환경:** StringBuilder (빠르고 가볍게)