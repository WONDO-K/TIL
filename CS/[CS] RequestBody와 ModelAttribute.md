# RequestBody VS ModelAttribute의 차이점
이들은 클라이언트 측에서 보낸 데이터를 Java 객체로 만들어주는데 ReqeustBody는 요청의 본문(Body)에 있는 값을 바인딩할 때 사용하고, ModelAttribute는 요청 파라미터나 multipart/form-data 형식을 바인딩할 때 사용한다.

## RequestBody
- 클라이언트가 보내는 요청의 본문을 자바 객체로 변환한다.
- 내부적으로 HttpMessageConverter를 거치는데, 이떄 ObjectMapper를 통해 JSON 값을 Java객체로 역직렬화 한다.
- 따라서 변환될 Java 객체에 기본 생성자를 정의해야 하고, getter나 setter를 선언해야 한다.
- cf.record에 기본 생성자를 따로 정의하지 않았는데 역직렬화가 되는 이유
    - record는 기본생성자를 자동으로 제공하지 않는 대신, '모든 필드를 초기화하는 생성자'를 제공한다.
    - jackson은 일반 객체와 달리, record를 역직렬화할 때는 '모든 필드를 초기화하는 생성자'를 사용해 역직렬화하기 때문이다.

## ModelAttribute
- 두가지 사용법
- 첫번째 사용법인 메서드 단에서의 사용법은 jsp의 Model에 하나 이상의 속성을 추가하고 싶을 때 사용한다.
    - e.g. model.addAttribute(“속성 이름”, “속성 값”)
- 두번째 사용법인 인자 단에서의 사용으로 클라이언트가 보내는 요청의 파라미터나 multipart/form-data 형식의 데이터를 자바 객체로 변환한다.
- 내부적으로 ModelAttributeMethodProcessor를 거치는데, 이때 지정된 클래스의 생성자를 찾아 객체롤 변환한다.

---

## 추가적으로 알아두면 좋은 내용

### RequestBody와 관련된 보완 지식
- `@RequestBody`는 주로 JSON, XML 등의 구조화된 데이터를 처리할 때 사용되며, `Content-Type`이 `application/json`인 요청에서 작동한다.
- 기본적으로 `@RequestBody`는 요청 본문 전체를 읽기 때문에, 하나의 컨트롤러 메서드에서는 하나만 사용할 수 있다. 여러 개를 사용하면 `HttpMessageNotReadableException`이 발생할 수 있다.
- 유효성 검사를 위해 `@Valid` 또는 `@Validated`와 함께 사용할 수 있으며, 이때 `BindingResult`를 인자로 추가하여 유효성 검사 실패 시 예외가 발생하지 않도록 처리할 수 있다.

### ModelAttribute와 관련된 보완 지식
- `@ModelAttribute`는 요청 파라미터를 통해 객체를 구성하므로, `Content-Type`이 `application/x-www-form-urlencoded` 또는 `multipart/form-data`인 경우에 주로 사용된다.
- HTML Form을 통해 전송된 값이나 쿼리 스트링의 값을 자동으로 객체 필드에 바인딩한다.
- Spring은 `@ModelAttribute`가 생략되더라도 기본적으로 파라미터에 해당하는 객체를 자동으로 생성해 바인딩한다. 따라서 명시하지 않아도 동작하지만, 가독성과 명확성을 위해 사용하는 것이 좋다.
- 유효성 검사를 위해 `@Valid`, `@Validated`도 함께 사용할 수 있으며, 역시 `BindingResult`로 오류를 처리할 수 있다.

### 실무에서의 선택 기준
- **JSON 등의 구조화된 데이터를 클라이언트가 보낼 경우** → `@RequestBody` 사용
- **Form 데이터나 URL 쿼리 파라미터로 들어오는 경우** → `@ModelAttribute` 사용
- 단, `@RequestBody`와 `@ModelAttribute`는 서로 병행하여 사용할 수 없으며, 각각의 특성과 요청 형식에 따라 선택적으로 사용해야 한다.

### 면접에서 이렇게 나올 수 있어요
💬 “@RequestBody와 @ModelAttribute의 내부 동작 차이를 설명해주세요.”
➡ @RequestBody는 HTTP 요청 본문 전체를 HttpMessageConverter를 통해 역직렬화하여 Java 객체로 변환합니다. 주로 JSON과 같은 구조화된 데이터에 사용되며, 내부적으로 ObjectMapper를 활용합니다. 반면 @ModelAttribute는 요청 파라미터(쿼리 스트링, form 데이터 등)를 기반으로 ModelAttributeMethodProcessor가 바인딩 작업을 수행하며, Setter 또는 생성자를 통해 객체를 구성합니다. 즉, 데이터의 출처와 바인딩 방식에서 차이가 있습니다.

💬 “폼 전송과 JSON 전송을 처리할 때 각각 어떤 어노테이션을 사용하고, 그 이유는 무엇인가요?”
➡ 폼 전송(form-data, URL-encoded)은 키-값 쌍으로 전달되므로 @ModelAttribute를 사용하는 것이 적절합니다. Spring이 파라미터 이름과 객체 필드를 자동 매핑해주기 때문입니다. 반면 JSON은 본문 전체를 직렬화한 형태이기 때문에, @RequestBody를 통해 HTTP Body의 내용을 객체로 변환해 주어야 합니다.

💬 “record 타입 DTO를 @RequestBody로 받을 수 있는 이유는?”
➡ Java record는 모든 필드를 초기화하는 생성자를 자동으로 제공합니다. Spring에서 @RequestBody는 내부적으로 Jackson의 ObjectMapper를 사용하는데, 이 경우 필드 기반 접근이 아닌 생성자 기반 역직렬화를 수행합니다. 따라서 Setter가 없어도, record 타입을 @RequestBody로 받을 수 있는 것입니다.

---

## 간단한 예시 코드

### ✅ @RequestBody 예시 (JSON 요청 처리)

```java
@RestController
public class UserController {

    @PostMapping("/users/json")
    public ResponseEntity<String> createUser(@RequestBody UserDto userDto) {
        return ResponseEntity.ok("Received name: " + userDto.getName());
    }
}

class UserDto {
    private String name;
    // getter, setter 생략
}
```

📌 클라이언트 요청 예시 (Postman 등에서 JSON 요청):
```json
POST /users/json
Content-Type: application/json

{
  "name": "Dongho"
}
```

---

### ✅ @ModelAttribute 예시 (Form-data 요청 처리)

```java
@Controller
public class UserFormController {

    @PostMapping("/users/form")
    @ResponseBody
    public String createUser(@ModelAttribute UserForm userForm) {
        return "Received name: " + userForm.getName();
    }
}

class UserForm {
    private String name;
    // getter, setter 생략
}
```

📌 클라이언트 요청 예시 (HTML form 또는 Postman의 x-www-form-urlencoded):

```
POST /users/form
Content-Type: application/x-www-form-urlencoded

name=Dongho
```

---

💡 위 두 방식은 데이터 포맷과 전송 방식에 따라 선택적으로 사용됩니다.