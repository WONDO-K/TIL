# @ControllerAdvice
모든 컨트롤러에 대해 전역 기능을 제공하는 어노테이션.
@ControllerAdvice가 선언된 클래스에 @ExceptinHandler, @InitBinder @ModelAttribute를 등록하면 예외 처리, 바인등 등을 한 곳에서 처리할 수 있어, 코드의 중복을 줄이고 유지보수성을 높일 수 있다.
@ControllerAdvice는 내부에 @Component가 포함되어 있어 컴포넌트 스캔 과정에서 빈으로 등록된다.
@RestControllerAdvice는 내부에 @ResponseBody를 포함하여 @ExceptionHadler와 함께 사용될 때 예외 응답을 JSON으로 내려준다.

---

## 💡 기타 유용한 기능

### 1. `@InitBinder`
- 설명: 컨트롤러에 전달되는 파라미터를 바인딩하거나 포맷을 지정하는 데 사용됩니다. 예를 들어 날짜 형식을 지정하거나 커스텀 에디터를 등록할 수 있습니다.
- 예시 코드:
```java
@ControllerAdvice
public class GlobalBinder {

    @InitBinder
    public void initBinder(WebDataBinder binder) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
        binder.registerCustomEditor(Date.class, new CustomDateEditor(dateFormat, false));
    }
}
```

### 2. `@ModelAttribute`
- 설명: 컨트롤러 메서드가 실행되기 전에 모델에 공통으로 포함되어야 할 데이터를 등록할 수 있습니다.
- 예시 코드:
```java
@ControllerAdvice
public class GlobalModelAttribute {

    @ModelAttribute("common")
    public String addCommonAttribute() {
        return "공통 모델 데이터";
    }
}
```

- 사용 예:
```java
@Controller
public class SampleController {
    @GetMapping("/hello")
    public String hello(Model model) {
        // model에는 이미 "common"이라는 키가 포함됨
        return "hello";
    }
}
```

---

이러한 기능들을 `@ControllerAdvice`에 함께 정의하면, 애플리케이션 전역에서 중복 없이 일관된 처리가 가능해집니다.

---

## 🔍 추가 설명 및 예시 코드

### 1. 언제 사용하나요?
- 예외 처리 로직을 컨트롤러마다 중복해서 작성하는 대신, 하나의 클래스에서 공통 처리하고자 할 때 사용됩니다.
- 로깅, 파라미터 바인딩 전처리, 공통 모델 속성 주입 등의 전역 처리 로직에 유용합니다.

### 2. 핵심 어노테이션
- `@ExceptionHandler`: 특정 예외를 처리하는 메서드에 사용합니다.
- `@InitBinder`: 컨트롤러에 들어오는 요청 파라미터를 변환하거나 초기화할 때 사용합니다.
- `@ModelAttribute`: 컨트롤러의 모든 요청 전에 공통으로 참조할 모델 데이터를 설정합니다.

### 3. 실무 예시

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<String> handleIllegalArgument(IllegalArgumentException e) {
        return ResponseEntity
                .badRequest()
                .body("잘못된 요청입니다: " + e.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleException(Exception e) {
        return ResponseEntity
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body("서버 오류가 발생했습니다.");
    }
}
```

### 4. 실무에서의 활용 포인트
- 서비스 로직에서 예외 발생 시, `throw new IllegalArgumentException("잘못된 입력")`와 같이 예외를 던지면 `@RestControllerAdvice`에서 자동으로 처리됩니다.
- 다양한 예외에 대해 공통적으로 JSON 응답 포맷을 지정할 수 있으므로, API 일관성을 유지하는 데 도움이 됩니다.

### 5. 면접에서 나올 수 있는 질문
- `@ControllerAdvice`와 `@RestControllerAdvice`의 차이는?
  → `@RestControllerAdvice`는 `@ResponseBody`가 포함되어 있어 JSON 형태의 응답을 반환합니다.
- 전역 예외 처리의 장점은 무엇인가요?
  → 코드 중복 제거, 응답 일관성 유지, 유지보수 용이성 향상 등입니다.