# @OneToOne 연관관계에서 Lazy Loading을 설정할 때 주의할 점은 무엇인가?
양방향 @OneToOne일 때 연관관계의 주인이 아닌 엔티티를 조회할 경우 Lazy Loading이 동작하지 않는다.

- JPA는 연관된 엔티티가 없으면 null로 초기화하고, 있으면 Lazy Loading이 설정되어 있을 경우 프록시 객체로 초기화한다.
- 하지만 DB의 테이블 관점에서 보면, 연관관계의 주인이 아닌 엔티티는 연관관계를 참조할 FK가 없기 떄문에 연관관계의 존재 여부를 알지 못한다.
- 그래서 JPA는 null 혹은 프록시 객체 중 무엇을 초기화할지 결정할 수 없게 되고, 결과적으로 연관된 엔티티의 존재 여부를 확인하는 추가 쿼리를 실행하기 때문에 Lazy Loading이 동작하지 않는다.
- JPA의 한계이기 때문에 단방향으로 모델링하거나 Lazy Loading이 정말 필요한 것인지 검토가 필요하다.

```java
@Entity(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne(mappedBy = "user", fetch = FetchType.LAZY)
    private Account account;
}

@Entity
public class Account {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne(fetch = FetchType.LAZY)
    private User user;
}

/////////////////////////////////////////////////////////

@Test
void lazyTest() {
    userRepository.save(new User());

    userRepository.findById(1L).orElseThrow(); // -> 여기 까지는 user만 조회하기 때문에 추가 작업이 없음
    // 코드 추가
    Account acc = user.getAccount(); // -> 여기서 추가 쿼리가 발생 -> Lazy Loading 붕괴
}
```
### 코드 설명
- @OneToOne(mappedBy = "user") → User는 연관관계의 주인이 아님
- Account는 User에 대한 외래 키(FK) 를 가지고 있으므로 연관관계의 주인
- Account acc = user.getAccount(); -> 외래키 컬럼이 없어서 연관 엔티티가 무엇인지 판단 불가
    - 그러므로 JPA 입장에서는 연관된 Account가 있는지 확인하는 작업이 필요함
    - "select * from account where user_id = ?" 같은 쿼리가 동작해야함
    - 이렇게 되면 즉시 로딩 (Eager) 처럼 동작해버린다.
