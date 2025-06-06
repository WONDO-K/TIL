# Filter와 Interceptor의 차이
## Filter
- 요청 및 응답의 전처리와 후처리를 수행하고 서블릿 컨테이너에 의해 실행되는 Java 클래스.
주로 유청 로깅, 인증, 인코딩 설정, CORS 처리, 캐싱, 압축 등의 공통 기능을 구현하는 데 사용
### 특징
- Filter는 서블릿 컨테이너(예:Tomcat) 수준에서 동작한다.
모든 요청이 서블릿으로 전달되기 전에 Filter를 거친다.
- 생명 주기 : Filter는 doFilter 메서드를 통해 요청 및 응답을 처리한다.
FilterChain을 통해 다음 필터 또는 최종 서블릿으로 요청을 전달한다.
- 순서 : web.xml이나 @WebFilter 어노테이션을 통해 설정할 수 있으며, 필터의 순서는 성정 파일에서 정의한다.

## Interceptor
- 특정 핸들러 메서드 실행 전후에 공통 기능을 구현한다.
주로 요청 로깅, 인증, 권한 검사, 세션 검사, 성능 모니터링 등을 수행하는 데 사용한다.
### 특징
- Interceptor는 Spring MVC의 핸들러 수준에서 동작한다. Dispatcher Servlet이 컨트롤러를 호출하기 전에 Interceptor를 거친다.
- 생명 주기
    - preHandle : 컨트롤러의 메서드가 호출되기 전에 실행된다.
    - postHadle : 컨트롤러의 메서드가 실행된 후, 뷰가 랜더링되기 전에 실행된다.
    - afterCompletion : 뷰가 랜더링된 후 실행된다.
- 순서 : WebMvcConfiguer를 구현한 클래스에서 addInterceptors 메서드를 사용하여 설정한다.
인터셉터의 순서는 등록 순수에 따른다.