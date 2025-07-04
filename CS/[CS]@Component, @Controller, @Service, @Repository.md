# @Component, @Controller, @Service, @Repository
각각의 클래스를 특정 역할을 수행하는 Spring Bean으로 등록할 떄 사용된다.
각 어노테이션은 클래스가 어떤 역할을 하는지 명시적으로 나타내며, Spring의 @CoponentScan 기능을 통해 자동적으로 Bean으로 등록된다.
@Component, @Controller, @Service, @Repository 어노테이션은 내부적으로 @Component 어노테이션을 사용하고 있다.

## 특징과 용도
### @@Component
가장 일반적인 형태의 어노테이션으로, 특정 역할에 종속되지 않는 일반적인 Spring Bean을 나타낸다.
공통 기능을 제공하는 유틸리티 클래스나, 특정 계층에 속하지 않는 일반적인 컨포넌트를 정의할 때 사용된다.
### @Service
비즈니스 로직을 수행하는 클래스에 사용되며 서비스 레이어의 Bean을 나타낸다.
### @Controller 
Spring MVC에서 웹 요청을 처리하는 컨트롤러 클래스에 사용되며 프레젠테이션 레이어의 Bean을 나타낸다.
### @Repository
데이터베이스와의 상호작용을 수행하는 클래스에 사용되며, 데이터 엑셋 레이어의 Bean을 나타낸다.

## @Controller, @Repository 대신 @Component 사용할 수는 없을까?
Spring6(Boot 3) 이전 버전에서는 @Component + @RequestMapping으로도 Bean 및 핸들러로 등록되었다.
하지만 Spring 6 이후 부터 @Controller 외에는 핸들러로 등록하지 않아 웹 요청을 정상적으로 수행할 수 없다.

```java
public class RequestMappingHandlerMapping extends RequestMappingInfoHandlerMapping
		implements MatchableHandlerMapping, EmbeddedValueResolverAware {
    ...
    @Override
    protected boolean isHandler(Class<?> beanType) {
        return AnnotatedElementUtils.hasAnnotation(beanType, Controller.class); // 컨트롤러 애너테이션인지 확인
    }
    ...
}
```

@Repository를 @Component로 대체할 경우, 
PersistanceExceptionTransiationPostProcessor에 의해 예외가 DataAccessException으로 변환되지 않는다.
또 @Service, @Controller, @Repository는 각각 특정 계층을 나타내므로, 
AOP의 포인트컷을 정의할 때 유용하게 사용될 수 있다.
@Component를 사용하면 이러한 계층 구분이 불분명해져서 AOP 적용이 어려울 수 있다. 

---

# ✅ 추가적으로 알아야 할 내용 및 보완 설명

## 1. 스테레오타입 어노테이션의 의미
- `@Service`, `@Controller`, `@Repository`는 모두 `@Component`의 메타 어노테이션이다.
- 단순 Bean 등록뿐 아니라, **계층 명시**와 **특화 기능 제공**의 의미가 있다.

## 2. 계층 구분의 중요성
- AOP 적용 시 특정 계층만 로직을 적용하는 것이 중요하다.
- ex) `execution(* com.example..*Service.*(..))` → `@Service`에만 트랜잭션 적용
- 계층을 명시하지 않으면 향후 확장성과 유지보수성에 불리하다.

## 3. @Repository의 예외 변환
- `@Repository`는 `PersistenceExceptionTranslationPostProcessor`에 의해 JDBC, JPA, MyBatis 예외를 Spring 공통 예외인 `DataAccessException`으로 변환한다.
- 덕분에 데이터 접근 계층의 예외 처리가 일관되고, 상위 계층에서 특정 구현에 의존하지 않는다.

## 4. @Controller vs @RestController
| 어노테이션 | 설명 |
|-----------|------|
| `@Controller` | View 반환 (JSP, Thymeleaf 등) |
| `@RestController` | JSON 등 ResponseBody 반환 (API 개발) |

## 5. 스프링 빈의 스코프
| 스코프 | 설명 |
|--------|------|
| singleton (기본) | 애플리케이션당 1개 Bean |
| prototype | 요청 시마다 새 Bean |
| request | HTTP 요청당 새 Bean (웹) |
| session | 세션당 새 Bean (웹) |

## 6. Spring 6 변화 포인트
- Spring 6부터 `@Component` + `@RequestMapping` 방식 지원 중단
- 핸들러 등록 시 반드시 `@Controller` 사용 필요
- Spring Boot 3.x 대응 필요성

## 7. 핵심 요약 표
| 어노테이션 | 의미 | 특이사항 |
|------------|------|---------|
| `@Component` | 범용 Bean | 역할 불명확 |
| `@Service` | 비즈니스 로직 | 트랜잭션, AOP |
| `@Controller` | 웹 요청 | View 반환 |
| `@RestController` | REST API | JSON 반환 |
| `@Repository` | DB 접근 | 예외 변환 |