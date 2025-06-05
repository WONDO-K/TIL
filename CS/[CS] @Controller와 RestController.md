# @Controller 와 @RestController 의 차이점
주요 차이점은 HTTP 응답의 처리 방식

## @Controller
주로 View를 반환하는 컨트롤러를 정의할 때 사용한다.
메서드가 반환하는 값은 뷰 리졸버(View Resolver)에 의해 해석되어 JSP, Thymeleaf등과 같은 템플릿 엔진을 통해 HTML을 생성한다.

---

## @Controller 예시 (View 반환)

```java
@Controller
public class UserController {

    @PostMapping("/users/create")
    public String createUser(@RequestParam String name, Model model) {
        // 예시: 유저 생성 로직
        Long userId = userService.create(name); // 단순 예시
        model.addAttribute("id", userId);
        model.addAttribute("message", "User created successfully");
        return "userCreated"; // userCreated.html 뷰로 이동
    }
}
```

- 예시 입력: `POST /users/create?name=choi`

- 예시 출력: 뷰 렌더링 결과 (userCreated.html)
```html
<!DOCTYPE html>
<html>
<head><title>User Created</title></head>
<body>
    <p>ID: 10</p>
    <p>Message: User created successfully</p>
</body>
</html>
```

※ `userCreated.html`은 Thymeleaf 등 템플릿 엔진을 통해 렌더링되는 HTML 파일입니다.

## @RestController
주로 RESTful 웹 서비스 API를 정의할 때 사용한다.
메서드가 반환하느 값은 자동으로 JSON 또는 XML 형식으로 변환되어 HTTP 응답 본문에 포함된다.
이는 @Controller와 @ResponseBody의 결합된 형태

---

## @RestController + ResponseEntity 예시

```java
@RestController
public class ResponseEntityController {

    @PostMapping("/api/users")
    public ResponseEntity<Map<String, Object>> createUser(@RequestBody UserDto userDto) {
        // 예시: 유저 생성 로직 수행
        Long userId = userService.create(userDto);

        URI location = URI.create("/api/users/" + userId);
        Map<String, Object> responseBody = Map.of(
            "id", userId,
            "message", "User created successfully"
        );

        return ResponseEntity
                .created(location)         // HTTP 201 Created + Location 헤더
                .body(responseBody);       // JSON 본문 응답
    }
}
```

- 예시 입력: `POST /api/users` with JSON body
```json
{
  "name": "choi",
  "email": "choi@example.com"
}
```

- 예시 출력:
```
HTTP/1.1 201 Created
Location: /api/users/10
Content-Type: application/json

{
  "id": 10,
  "message": "User created successfully"
}
```