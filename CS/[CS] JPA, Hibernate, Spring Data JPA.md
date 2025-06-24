# JPA, Hibernate, Spring Data JPA 의 차이

## JPA
- JPA는 기술 명세다.
    - 자바 애플리케이션에서 관계형 데이터베이스를 사용하는 방식을 정의한 인터페이스이다.
    - JPA는 단순한 명세이기 때문에 인터페이스와 규약만 정의하며, 실제 구현체는 제공하지 않는다.
- Hibernate는 JPA의 구현체 중 하나.
    - JPA가 정의한 ```javax.persistence.EntityManager``` 와 같은 인터페이스를 직접 구현한 라이브러리이다.
    - JPA의 구현체 중 하나일 뿐이므로, DataNucleus, EclipseLink 등 다양한 JAP 구현체로 대체 가능
- Spring Data JPA는 JPA를 쉽게 사용할 수 있도록 지원하는 모듈이다.
    - JPA를 한 단계 추상화시킨 Respository라는 인터페이스를 제공한다.
    - 개발자가 Respository 인터페이스에 정해진 규칙대로 메서드를 만들어주기만 하면, 해당 메서드 이름에 적합한 쿼리를 날리는 구현체를 만들어 자동으로 Bean으로 등록해준다.
    - Spring Data JPA는 JPA를 기반으로 하며, 반복적인 코드 작성을 줄이고 데이터 접근 계층을 단순화 한다.
    이때 JPA를 추상화 했다는 의미는, Spring Data JPA의 Repository의 구현에서 JPA를 사용하고 있다는 것이다. 예를 들어 Repository 인터페이스의 기본 구현체인 ```SimpleJpaResporitory```는 내부적으로 ```EntityManager```를 사용한다.

---

### ✅ 실무에서는 EntityManager보다 Repository를 더 자주 써요

- 실무에서는 직접 `EntityManager`를 사용하는 경우보다, Spring Data JPA에서 제공하는 `JpaRepository` 인터페이스를 상속받아 사용하는 방식이 더 일반적입니다.
- Repository를 통해 기본적인 CRUD 작업은 물론, 메서드 이름만으로 쿼리를 자동 생성하는 기능까지 제공받을 수 있어 생산성이 뛰어납니다.

#### 🧪 예제 코드 - JpaRepository 사용 예시

```java
// 엔티티
@Entity
public class Member {
    @Id @GeneratedValue
    private Long id;
    private String name;
    private int age;

    // getters and setters
}

// Repository 인터페이스
public interface MemberRepository extends JpaRepository<Member, Long> {
    List<Member> findByName(String name); // 메서드 이름 기반 쿼리 자동 생성
}
```

```java
// 서비스 계층에서 사용 예
@Service
@RequiredArgsConstructor
public class MemberService {
    private final MemberRepository memberRepository;

    public void example() {
        // 저장
        Member member = new Member();
        member.setName("홍길동");
        member.setAge(30);
        memberRepository.save(member);

        // 조회
        List<Member> members = memberRepository.findByName("홍길동");
    }
}
```

#### 면접에서는 이렇게 나올 수 있어요
- “EntityManager 대신 JpaRepository를 사용하는 이유는?”
  👉 반복 코드 제거, 쿼리 자동 생성, 페이징 처리 지원 등 생산성 향상이 가장 크며, 기본적인 CRUD 외에도 `@Query`, `Querydsl` 등과 결합이 쉬움

- “JpaRepository는 내부적으로 어떻게 동작하나요?”
  👉 내부적으로는 `SimpleJpaRepository`가 구현체이며, 이 클래스는 결국 `EntityManager`를 주입받아 DB 연산을 수행함

---

## ✅ 보완하면 좋은 추가 내용

### 1. JPA는 ORM 명세다
- JPA는 객체지향 프로그래밍과 관계형 데이터베이스 사이의 패러다임 불일치 문제를 해결하기 위한 ORM(Object-Relational Mapping) 명세이다.
- 쉽게 말해, "자바 객체를 테이블처럼 다룰 수 있게 해주는 설계도"이다.

### 2. Hibernate는 JPA보다 많은 기능을 제공
- JPA 명세 외에도 Hibernate 고유 기능들이 많다 (예: `save()`, `merge()`, 2차 캐시, 통계 로그 등).
- 실무에서는 JPA 표준으로 개발하다가, Hibernate 고유 기능이 필요한 경우 직접 활용하기도 한다.

### 3. Spring Data JPA의 한계와 보완
- 메서드 이름 기반으로는 복잡한 동적 쿼리 작성이 어려움 → `@Query` 또는 Querydsl 등을 사용하여 해결
- Querydsl은 동적 쿼리를 타입 안정성 있게 작성할 수 있어 실무에서 많이 사용됨

### 4. 내부 구조와 작동 방식
- `JpaRepository` → `PagingAndSortingRepository` → `CrudRepository` 순으로 계층화되어 있음
- 실제 구현체는 `SimpleJpaRepository`이며, 내부적으로 `EntityManager`를 주입받아 동작함

### 5. 면접에서 이렇게 나올 수 있어요
- "Spring Data JPA는 어떤 식으로 JPA를 추상화하나요?"  
  👉 Repository 인터페이스를 정의하고, 메서드 이름 규칙에 따라 자동으로 구현체를 생성하여 EntityManager의 반복 사용을 감춘다.

- "JPA의 구현체로 Hibernate를 사용하는 이유는 무엇인가요?"  
  👉 Hibernate는 JPA 명세를 충실히 따르면서도 다양한 부가 기능(2차 캐시, 통계 등)을 제공하고, 성능과 커뮤니티 지원이 뛰어나기 때문에 널리 사용된다.

- "JPA의 1차 캐시는 무엇이며, 어떤 장점이 있나요?"  
  👉 동일한 트랜잭션 내에서 EntityManager는 같은 엔티티 객체를 반복 조회 시 캐시에 저장된 객체를 반환하여 성능을 향상시키고, 동일성 보장과 불필요한 쿼리 방지를 가능하게 한다.

### ✍️ 요약
- **JPA**: ORM 표준 명세
- **Hibernate**: JPA 구현체이자 독립 ORM 프레임워크
- **Spring Data JPA**: JPA 위에 추상화를 더한 생산성 도구