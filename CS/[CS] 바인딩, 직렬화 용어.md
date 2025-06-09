# 📘 바인딩, 직렬화, 역직렬화
## ✅ 바인딩 (Binding)

**정의:**  
HTTP 요청 데이터(form-data 또는 쿼리 스트링)를 자바 객체의 필드에 자동으로 매핑하는 것.
- 📌 쉽게 말해, 사용자가 보낸 데이터를 자바 코드에서 쓰기 좋게 객체에 자동으로 넣어주는 과정입니다.

**예시:**
```java
@PostMapping("/user")
public String createUser(@ModelAttribute User user) {
    // name=hong&age=20 → user.name = "hong", user.age = 20
}
```

**특징:**  
- `@ModelAttribute` 사용 시 기본 적용
- Spring이 Setter 또는 생성자를 통해 필드 값 자동 주입

---

## ✅ 직렬화 (Serialization)

**정의:**  
자바 객체를 네트워크 전송이나 저장을 위해 JSON, XML 등 문자열 형태로 변환하는 것.  
- 📌 쉽게 말해, 바인딩된 자바 객체의 각 필드 값을 문자열로 ‘풀어헤쳐서’ 네트워크로 보내기 좋게 만드는 과정입니다.  
  예를 들어, `User(name="dongho", age=30)` 이라는 객체를 JSON 형식으로 바꾸면 다음과 같이 직렬화됩니다:  
  {  
    "name": "dongho",  
    "age": 30  
  }

**예시:**
```java
User user = new User("dongho", 30);
```

직렬화 결과:
```json
{
  "name": "dongho",
  "age": 30
}
```

**활용:**  
- 컨트롤러의 반환값이 JSON으로 응답될 때
- 내부적으로 HttpMessageConverter가 사용됨

---

## ✅ 역직렬화 (Deserialization)

**정의:**  
JSON, XML 등의 데이터를 자바 객체로 다시 변환하는 것.
- 📌 쉽게 말해, 네트워크로 받은 문자열 데이터를 자바 객체로 다시 바꾸는 과정입니다.

**예시:**
```json
{
  "name": "dongho",
  "age": 30
}
```

```java
@PostMapping("/user")
public String createUser(@RequestBody User user) {
    // JSON 데이터를 자바 객체로 역직렬화
}
```

**활용:**  
- `@RequestBody` 사용 시 자동 적용
- 내부적으로 ObjectMapper 등 사용

---

## 🔄 비교 요약

| 개념       | 정의                              | 사용 예시                        | 관련 어노테이션       |
|------------|-----------------------------------|----------------------------------|------------------------|
| 바인딩     | 요청 파라미터 → 객체 매핑         | `@ModelAttribute`                | `@ModelAttribute`     |
| 직렬화     | 객체 → JSON 등으로 변환            | 컨트롤러 → 클라이언트 응답       | `@ResponseBody`       |
| 역직렬화   | JSON → 객체로 변환                 | 클라이언트 요청 → 컨트롤러 매핑 | `@RequestBody`        |

---

## 🧠 면접에서는 이렇게 나올 수 있어요

> 💬 “Spring에서 직렬화와 역직렬화는 언제 일어나나요?”

📌 **답변 예시:**  
Spring에서는 컨트롤러가 객체를 반환할 때, 해당 객체는 HttpMessageConverter를 통해 JSON 등으로 직렬화되어 응답됩니다. 반대로 클라이언트가 JSON 데이터를 전송하면 `@RequestBody`를 통해 역직렬화가 발생하여 자바 객체로 매핑됩니다.

---
