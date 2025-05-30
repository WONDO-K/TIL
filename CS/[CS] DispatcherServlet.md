# DispatcherServlet

Spring MVC의 핵심 구성 요소로, 프론트 컨트롤러(Front Controller) 역할을 수행하는 클래스입니다. 클라이언트의 요청을 받아 적절한 컨트롤러(Handler)로 위임하고, 응답을 생성해 다시 클라이언트에게 전달합니다.

## ✅ DispatcherServlet의 역할

1. **요청 수신**  
   클라이언트의 HTTP 요청을 가장 먼저 수신하는 진입점입니다.

2. **요청 라우팅**  
   `HandlerMapping`을 통해 요청 URL에 대응하는 컨트롤러(핸들러)를 찾습니다.

3. **핸들러 실행**  
   `HandlerAdapter`를 통해 실제 컨트롤러를 실행하고 결과(`ModelAndView`)를 받습니다.

4. **뷰 렌더링**  
   `ViewResolver`를 통해 어떤 뷰를 사용할지 결정하고, 최종적으로 뷰를 렌더링합니다.

5. **응답 반환**  
   렌더링된 뷰 결과를 HTTP 응답으로 만들어 클라이언트에 전달합니다.

## 🧩 연계 컴포넌트 정리

| 구성 요소         | 설명 |
|------------------|------|
| `HandlerMapping` | 어떤 컨트롤러가 요청을 처리할지 결정하는 역할 |
| `HandlerAdapter` | 컨트롤러 실행을 위한 어댑터 역할 (즉, 컨트롤러를 호출) |
| `ViewResolver`   | `ModelAndView`에 담긴 뷰 이름을 실제 뷰로 변환 |
| `Filter`         | DispatcherServlet 앞단에서 요청/응답 필터링 |
| `Interceptor`    | DispatcherServlet 앞/뒤에서 요청 전처리 및 후처리 수행 |

## 🧠 면접에서는 이렇게 나올 수 있어요

> 💬 “Spring MVC에서 DispatcherServlet이 하는 역할을 설명해주세요.”  
→ DispatcherServlet은 Spring MVC에서 프론트 컨트롤러 역할을 합니다. 클라이언트 요청을 수신하고, 적절한 컨트롤러를 찾아 실행한 뒤, 결과를 뷰로 렌더링해서 클라이언트에 응답합니다.

> 💬 “DispatcherServlet이 HandlerMapping, HandlerAdapter와 어떤 관계가 있나요?”  
→ DispatcherServlet은 요청을 처리하기 위해 먼저 HandlerMapping을 사용해 적절한 컨트롤러(핸들러)를 찾고, 그 다음 HandlerAdapter를 통해 해당 핸들러를 실행합니다.

> 💬 “Spring Boot에서 DispatcherServlet 설정을 따로 하지 않아도 동작하는 이유는?”  
→ Spring Boot는 자동 설정(AutoConfiguration) 기능을 통해 DispatcherServlet을 기본 빈으로 등록하고, `/` 경로에 매핑되도록 설정해줍니다. 따라서 별도의 XML이나 Java Config 없이도 작동합니다.

## 🔎 부가 설명

- DispatcherServlet은 `web.xml`에 명시적으로 등록하지 않아도 Spring Boot에서는 자동으로 등록됩니다.
- 다양한 타입의 컨트롤러(예: `@Controller`, `@RestController`)와도 연동됩니다.
- 요청 흐름 상에서 필터(Filter) → 인터셉터(Interceptor) → DispatcherServlet 순으로 실행됩니다.