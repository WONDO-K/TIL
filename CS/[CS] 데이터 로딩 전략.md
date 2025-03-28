# 데이터 로딩 전략 (Fetching Strategy)
- JPA의 Fetch 전략 설정에 해당하는 부분으로 연관된 엔티티를 즉시 로딩(Eager)할지 아니면 지연 로딩(Lazy) 결정하는 전략이다.

## Eager
- FetchType.EAGER
    - 연관된 엔티티를 즉시 함께 조회한다.
    - 쿼리 한 번에 조인해서 들고 오려 함
    - ex) select * from user left join account ...~~
## LAZY
- FetchType.LAZY
    - 연관된 엔티티를 실제 사용할 때까지 로딩을 미룬다.
    - 즉, 처음에는 프록시 객체를 반환하고
    - getAccount() 같은 접근 시점에 추가 쿼리를 발생시킨다.

## EAGER 와 LAZY 코드 상 흐름
```java
User ←→ Account

// EAGER
user = findById(1L);
↓
user.getAccount(); // 이미 로딩됨 (쿼리 1번에 둘 다 조회)

// LAZY
user = findById(1L); // user만 조회됨
↓
user.getAccount();   // 이 시점에 쿼리 날려서 account 조회
```

## 왜 EAGER가 기본이 아닌가?
- 순환 참조로 인해 스택 오버 플로우가 발생할 수 있다.
- 유연성이 떨어진다.
- JPA에서는 
    - @ManyToOne 기본 LAZY
    - @OneToOne, @OnetoMany는 기본 EAGER로 설정되어 있지만 실제로는 대부분 LAZY로 설정해서 사용한다.

## 주의할 점
- LAZY 설정했지만 EAGER 처럼 작동하는 경우
    - @Transactional 없이 LAZY 접근을 하면 예외 발생함(LazyInitializationException)
    - toString(), JSON 변환, 로그 찍기 등의 순간에 프록시 초기화가 발생한다 -. 쿼리 발생
- N+1 문제
    - LAZY가 의도치 않게 반복문을 돌 때마다 쿼리 발생하면 성능 저하
    - 해결책 : fetch, join, @EntityGraph, batch size

## 여기서 프록시란?
- 진짜 객체를 감싸고 있는 가짜 객체
    - 말 그대로 대리 객체의 역할을 수행
- Hibernate가 만든 가짜 클래스를 제공받고 추후에 실제 DB에 접근이 이루어 질때 진짜 DB에 접근하는 객체를 만들어준다.
```java
@Transactional
public User getUser() {
    return userRepository.findById(1L).orElseThrow();
}

// 트랜잭션 바깥
User user = service.getUser(); // -> user를 반환 받고 영속성 컨텍스트는 이미 죽은 상태
System.out.println(user.getAccount().getName()); // ❌ 여기서 예외! -> 영속성 컨텍스트가 죽은 경우에는 (DB 세션이 종료 된) 더 이상 DB 접근이 불가능해져서 예외 발생
```

## 예상 질문
1. Lazy 로딩의 장점은 뭔가요?
    - 현시점에 불필요한 데이터를 미리 불러오지 않아서 성능이 좋아질 수 있고, 메모리 사용량도 줄어든다.
2. 그럼 왜 Lazy 대신 Eager 사용하는 경우가 있죠?
    - 해당 연관 엔티티가 항상 같이 필요한 필수 데이터라면, Lazy로 두면 오히려 매번 쿼리를 추가로 발생시켜 성능이 더 나빠질 수 있다.
3. Lazy로 설정했는데도 Eager처럼 동작하는 경우가 있나요?
    - 연관관계의 주인이 아닌 쪽에서 Lazy를 설정할 경우 프록시를 사용할 수 없기 댸문에, 존재 여부 판단을 위해 추가 쿼리를 발생시키면서 사실상 Eager처럼 동작하게 된다.