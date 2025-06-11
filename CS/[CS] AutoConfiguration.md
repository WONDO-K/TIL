# 요약

Spring Boot의 AutoConfiguration은 `@EnableAutoConfiguration`을 통해 필요한 설정을 자동으로 로딩합니다.
이 어노테이션은 내부적으로 `@Import(AutoConfigurationImportSelector.class)`를 통해 자동 구성 클래스를 불러옵니다.
이를 통해 Spring Boot는 개발자가 설정하지 않아도 내부적으로 필요한 Bean 등을 자동으로 설정합니다.

# AutoConfiguration
AutoConfiguration의 시작은 @SpringBootApplication 어노테이션 안에 있는 @EnableAutoConfiguration 이라는 애노테이션이다.
@EnableAutoConfiguration은 @Import(AutoConfigurationImportSelector.class)를 통해 구성 클래스를 가져온다.

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@AutoConfigurationPackage
@Import({AutoConfigurationImportSelector.class})
public @interface EnableAutoConfiguration {
    String ENABLED_OVERRIDE_PROPERTY = "spring.boot.enableautoconfiguration";

    Class<?>[] exclude() default {};

    String[] excludeName() default {};
}
```
자동 구성 클래스를 가져올 때는 AutoConfigurationImportSelector 클래스의 selectImports(AnnotationMetadata annotationMetadata) 라는 메서드를 이용하고, getAutoConfigurationEntry(AnnotationMetadata annotationMetadata); 메서드를 통해 Import할 클래스가 무엇인지 알 수 있게 된다.
이 클래스는 내부적으로 `spring.factories` 또는 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` 파일에 정의된 자동 구성 클래스를 기준으로, 
조건에 맞는 설정을 선별하고 등록합니다. 
Spring Boot 2.7부터는 `spring.factories` 대신 새로운 경로를 사용할 수 있습니다.

## 간단한 메서드 동작 과정
- getCandidateConfigurations(annotationMetadata, attributes); - AutoConfiguration의 후보들을 가져온다.
- removeDuplicates(configurations); - 중복을 제거한다.
- getExclusions(annotationMetadata, attributes); - 자동 설정에서 제외되는 설정에 대한 정보를 가져온다.
- configurations.removeAll(exclusions); - 제외되는 설정을 제거한다.
- ㄴgetConfigurationClassFilter().filter(configurations); - 필터를 적용한다.

## 참고사항 및 알아두면 좋은 점

- 자동 구성 클래스는 보통 `@ConditionalOnClass`, `@ConditionalOnMissingBean` 등의 조건부 어노테이션으로 감싸져 있어, 
  클래스패스에 특정 라이브러리가 있거나 특정 Bean이 없을 경우에만 적용됩니다.
- 자동 구성이 어떻게 적용되는지 확인하려면 `spring-boot-autoconfigure` 모듈의 내용을 참고하거나, 
  `@SpringBootApplication`을 사용하는 프로젝트에서 `--debug` 옵션을 사용하여 어떤 자동 구성이 적용되었는지 확인할 수 있습니다.
- 자동 구성이 편리하지만, 원리를 이해하고 `exclude` 옵션으로 불필요한 구성을 제거하거나, 직접 설정을 오버라이드할 수 있는 능력이 중요합니다.

### 📘 각 항목별 간단 설명

- `@ConditionalOnClass`: 클래스패스에 특정 클래스가 있을 때만 자동 설정이 적용됩니다. 예: JDBC 관련 설정은 `JdbcTemplate`이 클래스패스에 있을 때만 적용됩니다.
- `@ConditionalOnMissingBean`: 특정 Bean이 존재하지 않을 경우에만 자동 설정이 적용됩니다. 개발자가 직접 Bean을 정의하면 해당 자동 설정은 적용되지 않습니다.
- `--debug` 옵션: Spring Boot 애플리케이션을 실행할 때 이 옵션을 사용하면, 어떤 자동 설정이 적용되었고, 어떤 설정이 제외되었는지 상세한 리포트를 확인할 수 있습니다.
- `exclude` 옵션: `@SpringBootApplication(exclude = { ... })` 또는 `application.yml` 설정을 통해 불필요한 자동 구성을 제거할 수 있습니다.

### ✅ 요약표

| 항목 | 설명 | 실무에서 중요성 |
|------|------|------------------|
| `@ConditionalOnClass` | 클래스가 존재할 때만 설정 적용 | 라이브러리 기반 조건 설정 |
| `@ConditionalOnMissingBean` | 직접 등록한 Bean이 없을 때만 적용 | 사용자 정의 우선 가능 |
| `--debug` 옵션 | 어떤 자동 설정이 적용되었는지 확인 | 디버깅 시 필수 도구 |
| `exclude` 옵션 | 자동 구성을 제거 가능 | 충돌 방지 및 커스터마이징 |