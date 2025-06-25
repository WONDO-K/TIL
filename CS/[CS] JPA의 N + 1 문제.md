# JPA의 N + 1 문제
JPA의 N + 1 문제는 연관 관계가 설정된 엔티티를 조회할 경우에, 조회된 데이터 개수(N)만큼 연관 관계의 조회 쿼리가 추가로 발생하는 현상이다. 예를 들어, 블로그 게시글과 댓글이 있는 경우, 게시글을 조회한 후 각 게시글마다 댓글을 조회하기 위한 추가 쿼리가 발생할 수 있다. -> 이를 N+1 문제라고 한다.

## findAll 메서드의 글로벌 패치 전략 별 N+1 문제 상황
> findAll는 Spring Data JPA가 제공하는 repository의 메서드
### 즉시 로딩의 경우
글로벌 패치의 전략을 즉시 로딩으로 설정하고 findAll()을 실행하면 N+1 문제가 발생한다.
이는 findAll()은 ```sql select u from User u ```라는 JPQL 구문을 생성해서 실행하기 때문이다.
JPQL은 글로벌 패치 전략을 고려하지 않고 쿼리를 실행한다. 모든 User를 조회하는 쿼리 실행 후, 즉시 로딩 설정을 보고 연관 관계에 있는 모든 엔티티를 조회하는 쿼리를 실행한다.

### 지연 로딩의 경우
글로벌 패치 전략을 지연 로딩으로 설정하고 findAll()을 실행하면 N+1 문제가 발생하지 않는다.
이는 연관 관계에 있는 엔티티를 실제 객체 대신에 프록시 객체로 생성하여 주입하기 때문이다.
하지만 프록시 객체를 사용할 경우에 실제 데이터가 필요하여 조회하는 쿼리가 발생하고 N+1 문제가 발생할 수 있다.

## N+1 문제 해결 방법은?
fetch join, @EntityGraph를 사용해 볼 수 있다.
### fetch join
연관관계에 있는 엔티티를 한번에 즉시 로딩하는 구문이다.
### @EntityGraph
@EntityGraph도 fetch join과 비슷한 효과를 만들어내며, 쿼리 메서드에 해당 어노테이션을 추가해 사용할 수 있다.

```sql
select distinct u
from User u
left join fetch u.posts
```

```java
@EntityGraph(attributePaths = {"posts"}, type = EntityGraphType.FETCH)
List<User> findAll();
```