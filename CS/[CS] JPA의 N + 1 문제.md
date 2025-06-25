# JPA의 N + 1 문제
JPA의 N + 1 문제는 연관 관계가 설정된 엔티티를 조회할 경우에, 조회된 데이터 개수(N)만큼 연관 관계의 조회 쿼리가 추가로 발생하는 현상이다. 예를 들어, 블로그 게시글과 댓글이 있는 경우, 게시글을 조회한 후 각 게시글마다 댓글을 조회하기 위한 추가 쿼리가 발생할 수 있다. -> 이를 N+1 문제라고 한다.

---

## ✅ N+1 문제의 본질적 차이 요약

- N+1 문제란, 부모 엔티티를 1번 조회한 뒤, 각 부모마다 자식 엔티티를 추가로 N번 조회하여 총 N+1개의 쿼리가 발생하는 현상을 말한다.

- 예: `User` 10명을 조회할 경우, `User` 1번 조회 + 각 User의 `posts` 10번 조회 = 총 11번 쿼리

- 반면, fetch join이나 @EntityGraph를 사용하면 1번의 조인 쿼리로 모든 User와 각 posts를 한 번에 가져올 수 있다.

✅ 즉, **“전체 정보를 가져오기 위해 쿼리를 여러 번 나누어 조회하느냐”**,  
✅ 아니면 **“한 번의 쿼리로 연관 데이터를 모두 가져오느냐”의 차이**다.

---

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
N+1 문제를 해결하기 위해 **fetch join**, **@EntityGraph**를 사용할 수 있다.

### ✅ fetch join
연관관계에 있는 엔티티를 한 번에 join하여 가져오는 JPQL 문법이다. 지연 로딩으로 인해 각 엔티티마다 추가로 발생하던 N개의 쿼리를 하나로 줄여준다.

```sql
SELECT DISTINCT u
FROM User u
LEFT JOIN FETCH u.posts
```

→ 위 쿼리는 모든 User와 각 User의 posts를 한 번에 조회한다. 쿼리 수를 1개로 줄여 N+1 문제를 해결할 수 있다.

### ✅ @EntityGraph
fetch join과 유사한 효과를 어노테이션 기반으로 낼 수 있는 방식이다. Spring Data JPA의 쿼리 메서드와 함께 사용하며, 내부적으로 fetch join 쿼리를 생성한다.

```java
@EntityGraph(attributePaths = {"posts"}, type = EntityGraph.EntityGraphType.FETCH)
List&lt;User&gt; findAll();
```

→ posts 관계를 조인해서 한 번에 조회하게 되어 N+1 문제를 방지한다.

---

## ❓ “결국 연관된 모든 데이터를 한 번에 가져오면 무거운 거 아닌가요?”

좋은 지적이다. fetch join이나 @EntityGraph는 쿼리 수는 줄이지만, **가져오는 데이터 양은 많아질 수 있다.**

특히 `@OneToMany` 같은 컬렉션 연관관계에서는 **중복된 결과**가 발생할 수 있어 주의해야 한다. 실제 서비스에서는 필요한 연관관계에만 fetch join을 적용하고, **불필요한 관계까지 조인하면 오히려 성능 저하**가 발생할 수 있다.

---

## ✅ 정리

| 구분 | 역할 | N+1 해결 여부 | 주의사항 |
|------|------|----------------|----------|
| fetch join | 연관 엔티티를 한 쿼리로 join | ✅ 해결 | 조인 결과 중복 주의 |
| @EntityGraph | fetch join을 어노테이션으로 표현 | ✅ 해결 | 단순 관계에 적합 |
| 지연 로딩 (Lazy) | 필요한 시점에 쿼리 발생 | ❌ N+1 유발 가능 | 트랜잭션 내 사용 필요 |

---

## 💬 면접에서는 이렇게 나올 수 있어요

> **Q. fetch join도 모든 연관 데이터를 한 번에 가져온다면, 결국 성능 부담 아닌가요?**

**A.**
```text
맞습니다. fetch join은 쿼리 수를 줄여주는 장점이 있지만, 모든 데이터를 조인하면 중복 행이나 부하가 생길 수 있습니다. 따라서 필요한 연관 관계에만 사용하고, 복잡한 컬렉션 구조에서는 페이징과 함께 사용하지 않도록 주의합니다. 상황에 따라 @BatchSize와 같은 대안도 고려할 수 있습니다.
```
---

## ✅ 실무에서 좋은 fetch join 사용 전략

### 1. 꼭 필요한 연관관계에만 fetch join 적용
- 실제 요청 시점에 조회가 필요한 연관관계만 fetch join
- 예: 게시글 목록에서는 작성자 정보까지만 필요 → `LEFT JOIN FETCH post.author`
- 사용자가 상세 페이지 클릭 시 → `LEFT JOIN FETCH post.comments`

> ❗ 전체를 다 조인하면 JOIN 수만큼 결과 행이 곱해져 중복 발생 → 메모리 낭비 + 페이징 불가

---

### 2. 컬렉션(@OneToMany)은 fetch join에 주의
- `@OneToMany`는 조인 시 중복 행 발생 → 페이징 불가, 결과 왜곡
- 해결 방법:
  - `@BatchSize(size = N)`로 지연 로딩된 엔티티들을 한 번에 조회
  - 조회 전용 DTO를 활용한 쿼리 분리

```java
// ❌ 잘못된 예시: OneToMany에 fetch join 사용 + 페이징
@Query("SELECT p FROM Post p LEFT JOIN FETCH p.comments")
Page<Post> findAll(Pageable pageable); // 실패: 페이징 불가
```

```java
// ✅ 대안: 페이징 + 연관관계는 @BatchSize로 나중에 조회
@BatchSize(size = 100)
@OneToMany(mappedBy = "post")
private List<Comment> comments;
```

---

### 🔍 추가 설명: @BatchSize와 Lazy 로딩 묶음 처리

```java
List<Post> posts = postRepository.findAll(PageRequest.of(0, 10));
for (Post post : posts) {
    post.getComments().size(); // 여기가 Lazy 로딩
}
```
- 위 코드는 `@BatchSize` 전략과 함께 사용되면 N+1 문제를 방지할 수 있는 대표적인 예시이다.
- `findAll()`을 통해 10개의 Post를 페이징 조회하면, 각 Post는 아직 comments를 조회하지 않고 프록시만 가짐.
- `post.getComments().size()`를 통해 Lazy 로딩이 트리거되면 Hibernate는 10개의 post ID를 한꺼번에 수집하여 다음과 같은 쿼리를 실행함:
- PageRequest.of(페이지 번호, 페이지 크기) -> 페이지 번호부터 시작 -> 페이지 크기 만큼 (0,10) -> 0번 페이지부터 최대 10개


```sql
SELECT * FROM comment WHERE post_id IN (1, 2, ..., 10)
```

- 이처럼 `@BatchSize(size = 100)` 설정 덕분에, 여러 개의 Lazy 로딩 대상이 하나의 쿼리로 묶여서 처리됨.
- 페이징과 Lazy 로딩을 동시에 만족하면서도 N+1 문제를 피할 수 있는 좋은 전략임.

💡 단, @BatchSize는 컬렉션뿐 아니라 ManyToOne 관계에도 적용 가능하며, FetchType.LAZY인 경우에만 작동함.

---

### 3. 상세 화면 vs 목록 화면 쿼리 분리
- 목록에서는 연관관계 최소화 (ex. 게시글 + 작성자)
- 상세에서는 필요에 따라 fetch join 또는 DTO 기반 custom 쿼리 작성

---

### 4. DTO로 필요한 데이터만 조회
- JPA의 Projection (`new dto(...)`)을 사용하여 필요한 컬럼만 조회

```java
@Query("SELECT new com.example.dto.PostSummaryDto(p.title, a.name) FROM Post p JOIN p.author a")
List<PostSummaryDto> findSummaryPosts();
```

---

### 5. Hibernate의 @NamedEntityGraph 활용
- 서비스별로 필요한 연관관계만 가져오도록 명시적인 EntityGraph 정의 가능

---

## 💬 면접에서는 이렇게 질문할 수 있어요

> **Q. 모든 연관관계를 fetch join으로 가져오면 되는 거 아닌가요?**

**A.**
```text
모든 연관관계를 fetch join하면 쿼리 수는 줄일 수 있지만, 중복된 결과가 발생하고 메모리 낭비가 생깁니다. 특히 OneToMany 관계에서는 페이징이 불가능해 성능 문제가 큽니다. 따라서 꼭 필요한 연관관계만 fetch join으로 가져오고, 나머지는 Lazy 로딩이나 DTO 기반 쿼리로 분리해 조회하는 전략이 중요합니다.
```