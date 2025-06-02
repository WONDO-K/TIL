# @ResponseBody가 있을 때와 없을 때
@ResponseBody 혹은 ResponseEntity<T> 반환을 사용한다면, 스프링은 컨트롤러에서 반환된 값을 HTTP 응답 본문에 직접쓴다.
이때 Java 객체를 자동으로 JSON이나 XML등의 타입으로 직렬화한다. 만약, 없는 경우에는 스프링은 반환값을 뷰 이름으로 해석한다.
뷰 이름으로 해석한 이후에, 뷰 리졸버를 사용해 뷰를 찾고 응답한다.(뷰에 전달할 모델이 있다면, 이를 뷰에 전달하고 응답한다.)

## @ResponseBody와 ResponseEntity<T> 어떤 방식이 더 좋은가?
- @ResponseBody를 사용하는 경우
    - 코드를 간결하게 유지할 수 있다.
    - 하지만, 상태코드와 헤더를 유연하게 변경하기는 어렵다.
- ResponseEntity<T> 반환의 경우
    - 상태코드와 헤더를 유연하게 변경할 수 있다.
    - 반대로 작성할 코드의 양이 증가한다.

---

## ✅ 예시 코드

### 1. @ResponseBody 예시
```java
@RestController
public class HelloController {
    
    @GetMapping("/hello")
    @ResponseBody
    public String hello() {
        return "Hello, World!";
    }
}
```
- 위 코드는 문자열 `"Hello, World!"`를 HTTP 응답 본문에 그대로 반환한다.
- `@RestController`는 내부적으로 `@Controller + @ResponseBody`를 포함한다.

### 2. ResponseEntity<T> 예시
```java
@GetMapping("/user")
public ResponseEntity<User> getUser() {
    User user = new User("dongho", 30);
    return ResponseEntity
            .status(HttpStatus.OK)
            .header("X-Custom-Header", "value")
            .body(user);
}
```
- JSON 응답 + 커스텀 헤더 설정 + 상태 코드 제어까지 가능하다.

---

## 💡 추가 개념: @RestController와의 관계

- `@RestController`는 클래스 레벨에서 `@Controller`와 `@ResponseBody`를 합친 어노테이션이다.
- `@RestController`를 사용하면, 클래스의 모든 메서드에 일일이 `@ResponseBody`를 붙이지 않아도 된다.

```java
@RestController
public class ApiController {
    @GetMapping("/info")
    public Info getInfo() {
        return new Info("ssafy", "backend");
    }
}
```

---


## 🧠 면접에서는 이렇게 나올 수 있어요

- "`@ResponseBody`와 `ResponseEntity`의 차이를 설명해주세요."
- "`@RestController`가 하는 역할은 무엇인가요?"
- "스프링에서 JSON 응답을 처리하는 흐름을 설명해주세요."

---

### 💬 `@ResponseBody`와 `ResponseEntity`의 차이를 설명해주세요.
`@ResponseBody`는 컨트롤러의 반환 값을 HTTP 응답 본문으로 직렬화해 전송하는 역할만 수행합니다. 반면, `ResponseEntity`는 응답 본문뿐 아니라 HTTP 상태 코드와 헤더도 함께 제어할 수 있는 객체입니다. 단순 응답에는 `@ResponseBody`가 편리하고, 커스텀 상태 코드나 헤더 설정이 필요한 경우 `ResponseEntity`가 적합합니다.

---

### 💬 `@RestController`가 하는 역할은 무엇인가요?
`@RestController`는 클래스 레벨에서 `@Controller`와 `@ResponseBody`를 합친 어노테이션입니다. 이 어노테이션이 붙은 클래스 내의 모든 메서드는 반환 값이 HTTP 응답 본문으로 처리되며, 별도로 `@ResponseBody`를 붙일 필요가 없습니다. 주로 RESTful API를 작성할 때 사용합니다.

---

### 💬 스프링에서 JSON 응답을 처리하는 흐름을 설명해주세요.
스프링은 `@ResponseBody` 또는 `@RestController`가 붙은 메서드의 반환 객체를 `HttpMessageConverter`를 통해 JSON으로 변환합니다. 클라이언트가 `Accept: application/json` 헤더를 보냈다면, Jackson 등의 메시지 컨버터가 Java 객체를 JSON으로 직렬화하여 응답 본문에 담습니다. 이 과정에서 Content Negotiation도 함께 작동할 수 있습니다.

---


## 🧩 연계해서 알면 좋은 개념

- **HttpMessageConverter**: Java 객체 <-> JSON 변환을 담당하는 핵심 컴포넌트
- **Content Negotiation**: 클라이언트의 요청 헤더에 따라 응답 타입(JSON/XML 등)을 조정하는 기능
- **ExceptionHandler + ResponseEntity**: 예외 상황에서도 유연한 응답 제어 가능

---

## ✅ HTTP 메서드별 응답 처리와 Location 헤더 사용 여부

| HTTP 메서드 | 사용 목적             | 상태 코드 예시     | Location 사용 여부 | 비고 |
|-------------|------------------------|---------------------|---------------------|------|
| POST        | 새 리소스 생성         | 201 Created         | ✅ 사용 (필수)       | 생성된 리소스 URI 명시 |
| GET         | 리소스 조회            | 200 OK              | ❌ 사용 안 함        | 리소스는 응답 본문에 포함 |
| PUT         | 리소스 전체 수정       | 200 OK, 204 No Content | ❌ 보통 사용 안 함 | 단, 리소스가 새로 생성되는 경우엔 201 + Location 사용 가능 |
| PATCH       | 리소스 일부 수정       | 200 OK, 204 No Content | ❌ 사용 안 함    |  |
| DELETE      | 리소스 삭제            | 204 No Content      | ❌ 사용 안 함        | 삭제 완료만 알리면 충분 |

---

## 🧠 면접에서는 이렇게 나올 수 있어요 (추가)

- “HTTP 상태코드 201 Created는 어떤 조건에서 사용하는 게 적절한가요?”

### 💬 답변 예시:
클라이언트가 POST 요청을 보내 서버가 리소스를 생성했을 때, 응답으로 201 Created 상태 코드와 함께 Location 헤더에 새로 생성된 리소스의 URI를 포함해야 REST 원칙에 맞습니다. 이는 클라이언트가 이후 해당 리소스를 조회하거나 수정할 수 있도록 안내하는 역할을 합니다.
---

## ✅ ResponseEntity<Void>; 활용 방식

### 개념 설명
`ResponseEntity<Void>;`는 응답 본문 없이 상태 코드와 헤더만 전달할 때 사용하는 방식입니다. 이는 REST 원칙에 충실하며, 응답 본문이 불필요한 상황에서 응답의 의미를 명확히 전달할 수 있습니다.

### 사용 예시

#### 1. 리소스 삭제 (DELETE 요청)
```java
@DeleteMapping("/users/{id}")
public ResponseEntity<Void>; deleteUser(@PathVariable Long id) {
    userService.delete(id);
    return ResponseEntity.noContent().build(); // 204 No Content
}
```

#### 2. 리소스 생성 후 본문 없이 URI 제공
```java
@PostMapping("/users")
public ResponseEntity<Void> createUser(@RequestBody User user) {
    Long userId = userService.save(user);
    URI location = URI.create("/users/" + userId);
    return ResponseEntity.created(location).build(); // 201 Created + Location 헤더
}
```

---

## 🧠 면접에서는 이렇게 나올 수 있어요 (추가)

- “ResponseEntity<Void>는 어떤 상황에서 사용하나요?”

### 💬 답변 예시:
`ResponseEntity<Void>`는 응답 본문이 필요하지 않은 상황에서 사용합니다. 예를 들어 DELETE 요청에 대한 응답으로는 `204 No Content`를 반환하는 것이 REST 원칙에 부합하며, 이때 `ResponseEntity<Void>`를 활용하면 응답 본문 없이도 의미 있는 상태 코드와 헤더만으로 응답을 전달할 수 있습니다.