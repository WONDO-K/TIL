# JPA에서 ID 생성 전략
JPA에서 ID를 생성하기 위해서는 직접 할당과 자동 할당을 사용할 수 있다.
직접할 당은 @Id 어노테이션만을 사용하여 id값을 직접 할당하는 방식이다.
반면, 자동 할당은 @Id와 @GeneratedValue를 함께 사용해서 원하는 키 생성 전략을 선택하는 방식이다.
@GeneratedValue의 stretagy 옵션을 통해 생성 전략을 설정할 수 있는데, 여기에 올 수 있는 값인 GeneratedType은 아래와 같다.

```java
@Target({ElementType.METHOD, ElementType.FIELD})  
@Retention(RetentionPolicy.RUNTIME)  
public @interface GeneratedValue {  
    GenerationType strategy() default GenerationType.AUTO;  
  
    String generator() default "";  
}

public enum GenerationType { 
	AUTO,
	IDENTITY,
	SEQUENCE, 
	TABLE
}
```

## 자동 생성 방식을 사용할 때 전략
### IDENTITY 전략
기본키 생성을 DB에 위임하는 전략. 주로 MySQL, PostgreSQL, SQL Server, DB2에서 사용된다.
해당 전략을 사용하면 엔티티를 생성할 때 쓰기 지연이 적용되지 않는다.
왜냐하면 JPA에서 엔티티를 영속하기 위해선 식별자가 필요한데, IDENTITY 전략에서는 이식별자가 DB에 저장되어야 할당되기 때문이다. 따라서 엔티티를 생성할 때 즉시 INSERT 쿼리가 실행되어야 한다.
이때 하이버네이트를 사용하는 경우에는 INSERT 쿼리의 결과를 다시 조회하지 않기 위해서 내부적으로 Statement,getGeneratedKeys를 사용한다.
추가로 IDENTITY 전략을 사용하면 배치 인서트가 불가하다는 점을 주의해야한다.

### SEQUENCE 전략
시퀀스 키 생성 전략을 지원하는 DB에서 사용할 수 있다.
데이터베이스 시퀀스랑, 유일한 값을 자동으로 생성하게 하는 객체이다.
auto_increment와 달리 초기 값과 한번에 증가할 크기를 설정할 수 있다.
어떤 시퀀스를 사용할 것인지를 @SequenceGenerator로 설정할 수 있다.
SEQUENCE 전략은 em.persist()를 호출하는 경우 먼저 데이터 베이스 시퀀스를 이용하여 식별자를 조회한다.
이후 조회한 식별자를 엔티티에 할당한 후에 엔티티를 영속성 컨텍스트에 저장한다.
트랜잭션을 커밋하여 플러시가 일어나면 엔티티를 저장한다는 점에서 IDENTITY와 차이가 있다.

### TABLE 전략
키 생성 전용 테이블을 만들어 시퀀스를 흉내내는 전략이다. 어떤 테이블을 사용할 것인지를 @TableGenerator로 설정할 수 있다. TABLE 전략은 값을 조회하면서 SELECT 쿼리를 사용하며 증가를 위해 UPDATE 쿼리를 사용한다.
SEQUENCE 전략보다 DB와 한번 더 통신한다는 점에서 성능이 안좋다는 단점이 있지만, 모든 DB에 적용할 수 있다는 장점이 있다.

### AUTO 전략
데이터베이스 방언에 따라서 IDENTITY, SEQUENCE, TABLE 중 하나를 자동으로 선택한다.
>@GeneratedValue의 strategy의 기본값은 AUTO이다.
만약 AUTO를 사요할 때 SEQUENCE나 TABLE 전략이 선택되면, 시퀀스나 키 생성용 테이블을 미리 만들어 두어야 한다.

---

## 요약: GenerationType.IDENTITY vs SEQUENCE

| 전략         | ID 생성 방식                | ID 생성 시점              | 영속성 컨텍스트 등록 시점 | INSERT 쿼리 발생 시점     | 쓰기 지연 가능 여부 |
|--------------|-----------------------------|----------------------------|-----------------------------|---------------------------|--------------------|
| `IDENTITY`   | DB가 자동 생성 (`auto_inc`) | INSERT 수행 후             | INSERT 직후                 | `persist()` 시점에 즉시 발생 | ❌ 불가능           |
| `SEQUENCE`   | DB 시퀀스를 통해 생성       | `persist()` 전에 조회      | ID 세팅 후 즉시 등록 가능     | flush 시점에 발생          | ✅ 가능             |

- `IDENTITY`: DB에 먼저 INSERT를 해야 ID를 알 수 있으므로, 영속성을 위해 바로 INSERT가 실행된다.
- `SEQUENCE`: DB 시퀀스에서 먼저 ID를 받아오기 때문에, INSERT 없이도 영속성 컨텍스트에 등록 가능하다.
- `SEQUENCE`는 `allocationSize` 설정을 통해 성능 최적화(미리 여러 개 ID 확보)도 가능하다.

---

## 💡 em.persist()란?

`em.persist(entity)`는 JPA의 EntityManager를 통해 엔티티를 **영속성 컨텍스트에 등록**하는 메서드이다.  
호출된 엔티티는 영속 상태가 되며, 트랜잭션 커밋 시점에 INSERT 쿼리가 실행된다.

### ✅ Spring Data JPA에서는 직접 호출하지 않아도 된다

실무에서 Spring Data JPA를 사용하는 경우, 대부분은 `JpaRepository`의 `save()` 메서드를 사용한다:
```java
memberRepository.save(new Member("dongho"));
```

이 `save()` 내부에서는 신규 엔티티인 경우 `em.persist()`를,  
이미 존재하는 엔티티인 경우 `em.merge()`를 자동으로 호출해준다.  
따라서 일반적인 개발에서는 `em.persist()`를 명시적으로 호출할 일이 거의 없다.

## 🔄 배치 인서트(Batch Insert)

배치 인서트는 여러 개의 INSERT SQL을 하나의 배치로 묶어 한 번에 전송하는 기법으로, 대량 데이터 처리 시 성능 최적화에 유리하다.

### ✅ 배치 인서트의 장점

- **DB 통신 횟수 감소**: 여러 INSERT 쿼리를 한 번에 전송
- **성능 향상**: 다량의 엔티티를 효율적으로 저장

### ❗ IDENTITY 전략에서는 배치 인서트 불가

`GenerationType.IDENTITY` 전략은 DB가 ID(PK)를 생성하기 때문에, JPA는 `persist()` 호출 시 즉시 INSERT 쿼리를 실행해야 ID를 알 수 있다.  
→ 따라서 INSERT를 모아서 한꺼번에 보내는 배치 인서트가 불가능하다.

### ✅ SEQUENCE 전략은 배치 인서트 가능

`SEQUENCE` 전략은 DB 시퀀스에서 ID를 **사전에** 조회하여 엔티티에 할당할 수 있다.  
→ 여러 엔티티를 모아 배치 인서트가 가능하고, `allocationSize`를 통해 ID를 블록 단위로 미리 확보하여 성능을 더욱 높일 수 있다.

### 💡 예시

```java
for (int i = 0; i < 1000; i++) {
    Member member = new Member("member" + i);
    em.persist(member); // IDENTITY면 매번 INSERT 실행, SEQUENCE면 배치 가능
}
```

- **IDENTITY**: `em.persist()` 시점마다 INSERT → 배치 불가
- **SEQUENCE**: ID를 미리 받아두고 모아서 INSERT → 배치 가능

### 🔧 Hibernate 배치 인서트 설정 예시

```properties
spring.jpa.properties.hibernate.jdbc.batch_size=50
spring.jpa.properties.hibernate.order_inserts=true
```

→ 50개씩 INSERT를 묶어서 전송함