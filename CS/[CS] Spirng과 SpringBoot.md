# Spring과 Spring Boot의 차이

## Spring
Spring은 Spring Framework의 핵심 모듈들을 기반으로 한 프레임 워크로 엔터프라이즈 애플리케이션 개발을 지원하기 위한 대규모 오픈 소스 프로젝트이다.
Spring Framework를 사용하기 위해서는 설정 파일 작성을 통한 스프링 컨테이너 구성, 필요한 빈 객체 등록 및 이존성 설정, 데이터베이스 연결, 트랜잭션 관리 등 다양한 설정을 개발자가 직접 수동으로 구성해야 했다.
따라서 프로젝트 초기화 과정에서 많은 설정과 의존성을 추가하게 되어 프로젝트는 시작하는데 시간이 많이 걸렸다.
또한 스프링을 통해 웹 애플리케이션을 구축하기 위해서는 별도의 WAS를 설치하고 설정해야 했다.

## SpringBoot
SpringBoot는 Spring의 문제점을 해결해주고, 더 쉽고 빠르게 스프링 애플리케이션을 개발할 수 있도록 해주는 도구이다.
SpringBoot를 사용하면 Spring에서 제공하는 여러 기능들을 자동으로 설정하여 개발자가 보다 쉽게 사용할 수 있도록 해준다.

# SpringBooT의 주요 특징
- 자동 설정(Auto Configuration)
    - Spring Boot는 애플리케이션의 설정을 자동으로 구성합니다.
    - @EnableAutoConfiguration, @SpringBootApplication 어노테이션을 통해 자동 설정을 활성화합니다.
- 의존성 관리 간소화
    - 특정 기능을 쉽게 추가할 수 있도록 여러 개의 라이브러리와 의존성을 하나의 패키지로 묶어 제공하는 starter 의존성 통합 모듈을 제공합니다.
    - 예: spring-boot-starter-web, spring-boot-starter-data-jpa, spring-boot-starter-security
- 내장 서버
    - Tomcat, Jetty, Undertow와 같은 내장 웹 서버를 제공하여, 애플리케이션을 독립 실행형 JAR 파일로 배포하고, 바로 실행할 수 있게 합니다.
    - 배포를 위해 War 파일을 생성해서 Tomcat에 배포할 필요 없으며, JAR 파일에는 모든 의존성 라이브러리가 포함되어 있어 외부 서버 없이도 애플리케이션을 실행할 수 있습니다.

---

✅ Spring과 Spring Boot 정리 시 부족했던 부분 및 꼭 알아야 할 내용

1. Spring = 프레임워크, Spring Boot = 프레임워크를 빠르게 구축할 수 있게 해주는 툴킷  
   • 단순히 “Spring의 확장”이 아니라 생산성 향상을 위한 개발 플랫폼에 가깝다는 점 명확히 해야 함.  
   • 면접에서는 이렇게 질문 나올 수 있어요:  
     “Spring Boot가 Spring Framework와 어떤 구조적 차이를 만들어내나요?”  
     → 단순한 설정 자동화 이상의 철학(Convention over Configuration)을 설명할 수 있어야 합니다.

---

2. 자동 설정 원리(Auto Configuration) 이해 부족  
   • @EnableAutoConfiguration은 클래스패스에 있는 라이브러리와 어노테이션 등을 스캔해 적절한 설정을 자동으로 구성  
   • 내부적으로는 spring.factories 파일 기반의 조건부 설정 클래스(@ConditionalOnXXX)들로 이루어짐  

🔎 왜 중요한가요?  
→ 설정이 자동으로 된다고 무작정 믿고 쓰면 안 됨.  
실무에서는 “어떤 설정이 자동으로 적용됐는지” 명시적으로 확인할 수 있어야 함 (/actuator/beans, debug=true 활용)

---

3. Spring Boot와 Spring MVC의 관계  
   • 많은 사람이 혼동함: Spring Boot는 “MVC 프레임워크”가 아니고, MVC 구조를 빠르게 띄울 수 있는 “런처” 역할  
   • Spring Boot + Spring Web Starter = Spring MVC 기반 웹 애플리케이션을 자동 구성해주는 조합

---

4. Spring Boot는 설정을 감춘다 — 그래서 설정을 더 잘 알아야 한다  
   • application.yml 또는 application.properties에 모든 설정이 들어감  
   • 초기에 쉬워 보이지만, 운영 환경 분리, 보안 설정, 프로파일 구성 등에서 실수 잦음

---

5. 프로젝트 구조 차이 예시

| 구분         | Spring                       | Spring Boot                                |
|--------------|------------------------------|---------------------------------------------|
| 설정 방식    | XML/자바 기반 수동 설정       | 어노테이션 및 자동 구성                    |
| 서버 구동    | 별도 WAS 필요                | 내장 서버 포함 (Tomcat 등)                 |
| 설정 파일    | 다양한 XML 필요              | application.yml 하나로 통일 가능           |
| 실행 방식    | War 파일 + 배포              | Jar 파일만으로 실행 가능 (java -jar)      |

---

✍️ 마무리

Spring Boot는 빠르게 시작하기 위한 도구일 뿐, Spring에 대한 이해는 더 깊어야 합니다.  
면접에서는 “Spring Boot 덕분에 설정을 몰라도 쉽게 개발했어요”보다는  
👉 “Spring MVC 구조와 동작을 이해한 상태에서, Boot는 단순히 생산성을 높여준 툴입니다” 라고 말할 수 있어야 신뢰를 얻습니다.

---

## ✅ Spring MVC 구조와 DispatcherServlet 흐름 정리

Spring MVC는 Model-View-Controller 아키텍처를 기반으로 한 웹 애플리케이션 프레임워크입니다. 클라이언트 요청이 들어왔을 때 DispatcherServlet이 중심이 되어 흐름을 제어합니다.

### 📌 Spring MVC 핵심 구성요소
| 구성요소             | 설명 |
|---------------------|------|
| **DispatcherServlet** | 모든 요청을 중앙에서 받아 컨트롤러에 전달하고 응답까지 처리하는 프론트 컨트롤러 |
| **HandlerMapping**   | 요청 URI에 알맞은 컨트롤러(Handler)를 찾아주는 역할 |
| **Controller**       | 비즈니스 로직 처리 후 모델과 뷰 이름을 DispatcherServlet에 반환 |
| **ModelAndView**     | 모델 데이터와 뷰 이름을 함께 전달하는 객체 |
| **ViewResolver**     | 뷰 이름을 실제 뷰(JSP 등)로 변환해주는 역할 |
| **View**             | 모델 데이터를 렌더링해 클라이언트에 응답 |

### 📊 전체 요청 흐름 (DispatcherServlet 중심)
1. 사용자의 요청이 DispatcherServlet으로 들어온다.
2. DispatcherServlet은 HandlerMapping을 통해 요청에 맞는 컨트롤러를 찾는다.
3. 해당 컨트롤러가 요청을 처리하고, ModelAndView 객체를 반환한다.
4. DispatcherServlet은 ViewResolver를 통해 뷰 이름에 해당하는 View 객체를 찾는다.
5. View 객체는 모델 데이터를 기반으로 실제 응답을 렌더링한다.
6. 최종 결과를 DispatcherServlet이 클라이언트에게 응답으로 전달한다.

### 💡 면접에서는 이렇게 질문 나올 수 있어요:
- "Spring MVC 요청 흐름을 설명해주세요."
- "DispatcherServlet이 어떤 역할을 하나요?"
- "ViewResolver는 왜 필요한가요?"

👉 **실무 팁**: 
- `@Controller`, `@RestController`, `@RequestMapping`, `@ResponseBody` 등은 모두 이 구조 위에서 동작합니다.
- DispatcherServlet은 `web.xml` 또는 Spring Boot에서는 자동으로 등록되며, 서블릿 설정의 진입점입니다.
- Spring Boot에선 `spring-boot-starter-web` 의존성만 추가해도 Spring MVC 구조가 자동 설정됩니다.