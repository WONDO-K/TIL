


# 필터 체인 (Filter Chain)

## ✅ 필터 체인이란?
Filter Chain은 여러 개의 필터를 순차적으로 연결하여, 클라이언트의 요청(Request)이나 서버의 응답(Response)에 대해 공통된 처리를 수행할 수 있도록 해주는 구조입니다. 각 필터는 `doFilter()` 메서드를 통해 다음 필터로 요청을 전달하거나 중단할 수 있습니다.

> 쉽게 말해:  
> 요청 → 필터A → 필터B → 필터C → 서블릿(DispatcherServlet) → 응답 ← 필터C ← 필터B ← 필터A

---

## ⚙️ 서블릿의 필터 체인
- `javax.servlet.FilterChain` 기반
- DispatcherServlet 이전에 실행
- 주요 용도: 인코딩 설정, 인증 검사, 로깅, CORS 처리 등

예시 흐름:
```
클라이언트 → EncodingFilter → AuthFilter → DispatcherServlet → Controller
```

---

## 🔐 Spring Security의 필터 체인
- `SecurityFilterChain` 구조로 구성
- DispatcherServlet보다 먼저 실행됨
- 다양한 보안 필터가 순차적으로 연결되어 있음

### Spring Security 주요 필터 예시

| 필터명 | 역할 |
|--------|------|
| `UsernamePasswordAuthenticationFilter` | 로그인 인증 처리 |
| `JwtAuthenticationFilter` (사용자 정의) | JWT 토큰 검사 |
| `CsrfFilter` | CSRF 보호 |
| `ExceptionTranslationFilter` | 예외 처리 및 리다이렉트 |

---

## 🧩 Filter vs Interceptor

| 항목 | Filter | Interceptor |
|------|--------|-------------|
| 위치 | DispatcherServlet 이전 | DispatcherServlet 이후, Controller 전후 |
| 인터페이스 | `jakarta.servlet.Filter` | `HandlerInterceptor` |
| 적용 범위 | 서블릿 전역 | 스프링 컨트롤러 |
| 주 사용 목적 | 요청 인코딩, 인증, 로깅 | 권한 체크, 로그인 사용자 확인 |
| 특징 | 요청/응답 수정 가능 | 핸들러 접근 및 세부 제어 가능 |

---

## 🧠 핵심 요약
- 필터 체인은 클라이언트의 요청을 처리하는 과정에서 여러 필터가 순차적으로 적용되는 구조다.
- 서블릿 필터와 Spring Security 필터는 유사하지만 동작 위치와 구현 방식이 다르다.
- 실무에서는 Spring Security의 필터 체인을 구성하는 경험이 중요하게 다뤄진다.

---

## 💬 면접에서는 이렇게 나올 수 있어요

- “Filter와 Interceptor의 차이를 설명해보세요.”
- “Spring Security에서 필터 체인을 어떻게 구성했는지 설명해보세요.”
- “DispatcherServlet보다 먼저 동작하는 보안 처리는 어디서 이뤄지나요?”