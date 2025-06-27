# ✅ 이 페이지는 Spring Data JPA 실무 환경을 고려하여 EntityManager 예시와 Spring 방식의 비교를 함께 정리한 문서입니다.
# 엔티티 매니저
엔티티 매니저에 대해 알기 위해선 영속성 컨텍스트에 대해 이해해야 한다.
## 영속성 컨텍스트
엔티티를 영구 저장하는 환경으로 1차 캐싱, 쓰기 지연, 변경 감지를 통해 영속 로직을 효율적으로 할 수 있게 도와준다.
이러한 효율적인 영속 로직 수행을 위해서는 엔티티는 영속성 컨텍스트에 관리되어야 한다.
이런 작업을 도와주는 것이 엔티티 매니저다. 엔티티 매니저는 엔티티의 상태를 변경하고, 영속성 컨텍스트와 상호작용함으로써 영속 로직을 수행하는 역할을 가지고 있다.

## 구체적인 엔티티 매니저의 역할
엔티티는 영속성 컨텍스트와 관련하여 4가지 상태(비영속, 영속, 준영속, 삭제)를 가질 수 있다. 엔티티 매니저는 persist, merge, remove, close 메서드를 이용하여 엔티티의 상태를 변경할 수 있다. 또한, 엔티티 매니저는 영속성 컨텍스트의 1차 캐시로부터 엔티티를 조회할 수 있으며, 쓰기 지연 저장소에 있는 쿼리들을 flush하여 DB와 동기화시킬 수 있다. 또한 JPQL이나 Native Query를 이용해 직접 DB로부터 데이터를 불러올 수도 있다.

### 엔티티의 각 상태
```java
Member memeber = new Member("동까")
```
비영속 상태는 엔티티 객체가 새로 생성되었지만, 아직 영속성 컨텍스트와 연관되지 않은 상태이다.
이 상태에서는 데이터베이스와 전혀 관련이 없으며, 엔티티 객체는 메모리 상에만 존재한다.

```java
em.persist(member);
em.merge(detagedMember);
em.find(Member.class,1L);
```
영속 상태는 엔티티 객체가 영속성 컨텍스트에 관리되고 있는 상태이다.
이 상태에서는 엔티티의 변경 사항이 자동으로 데이터베이스에 반영된다.

```java
em.detach(member);
em.clear();
em.close();
```
준영속 상태는 엔티티 객체가 한 번 영속성 컨텍스트에 의해 관리되었지만, 현재는 영속성 컨텍스트와 분리된 상태이다. 이 상태에서는 엔티티 객체의 변경 사항이 더 이상 데이터베이스에 반영되지 않는다. 영속성 컨텍스트 종료, 트랜잭션 종료 등으로도 준영속 상태로 전환된다.

💡 추가 설명: Lazy 로딩과 준영속 오류

준영속 상태에서는 엔티티가 영속성 컨텍스트와 분리되어 있으므로, 지연로딩(Lazy Loading) 속성을 가진 연관 객체에 접근하려 하면 `LazyInitializationException`이 발생할 수 있다.  
예를 들어, 서비스 계층에서 트랜잭션이 종료된 후 컨트롤러에서 `member.getTeam().getName()`처럼 연관 객체를 조회하려고 하면, 해당 시점에는 영속성 컨텍스트가 없기 때문에 오류가 발생한다.

✅ 해결 방법: DTO로 변환하여 반환  
서비스 계층에서 엔티티를 DTO로 변환하면, 필요한 연관 객체를 미리 로딩(Lazy → Eager)하게 되어 컨트롤러에서 안전하게 사용할 수 있습니다.

```java
em.remove(member);
```
삭제 상태는 엔티티 객체가 영속성 컨텍스트에서 제거된 상태이다. 이 상태에서는 엔티티 객체가 데이터베이스에서 삭제된다.

### ✅ EntityManager 방식과 Spring Data JPA 방식 비교

| 엔티티 상태 | EntityManager 예시 코드 | Spring Data JPA 예시 코드 | 설명 |
|------------|--------------------------|-----------------------------|------|
| 비영속 | `Member m = new Member("동까");` | `Member m = new Member("동까");` | 단순 객체 생성. 아직 영속성 컨텍스트와 무관 |
| 영속 | `em.persist(m);` | `memberRepository.save(m);` | 저장 요청. Spring에서는 save가 persist/merge 포함 |
| 준영속 | `em.detach(m);` `em.clear();` | **직접 사용 X**, 보통 트랜잭션 종료로 인해 발생 | 컨트롤러 밖에서 lazy loading 하다 오류 발생할 수 있음 |
| 삭제 | `em.remove(m);` | `memberRepository.delete(m);` | 엔티티 삭제 요청 |


---

### 🔍 면접에서는 이렇게 질문 나올 수 있어요:

> Q. EntityManager를 직접 사용하는 코드와 Spring Data JPA가 내부적으로 수행하는 동작은 어떤 차이가 있나요?

✅ 답변 예시:  
Spring Data JPA는 EntityManager를 추상화한 JpaRepository 기반의 방식으로, 개발자가 직접 persist, remove, flush 등을 호출하지 않아도 내부에서 자동으로 처리됩니다. 예를 들어, save()는 내부적으로 persist 혹은 merge가 실행되며, delete()는 remove를 호출합니다. 이로 인해 트랜잭션 관리 및 영속성 컨텍스트와의 상호작용이 간결해집니다. 하지만 복잡한 쿼리 최적화나 트랜잭션 경계를 명확히 제어할 필요가 있을 때는 EntityManager를 직접 사용하는 경우도 있습니다.

---

### 💡 실무 팁

- `@Transactional`의 경계 내에서 save, delete, find 등을 사용하면 엔티티 상태 관리는 자동으로 이루어짐
- 하지만 Lazy 로딩 객체를 컨트롤러 레이어로 넘기면 오류 발생 가능 → DTO 변환 필수
- `flush()`는 강제 동기화, `clear()`는 컨텍스트 비움 → 거의 직접 쓸 일 없음

---

### ✅ DTO를 서비스 단에서 변환하고 컨트롤러로 넘기는 이유

엔티티를 그대로 컨트롤러로 반환할 경우, Lazy 로딩된 필드에 접근하면 트랜잭션 종료 후 예외가 발생할 수 있습니다. 이를 방지하기 위해 서비스 계층에서 DTO로 변환하고, 컨트롤러는 그 DTO만 응답으로 반환하는 것이 안전한 구조입니다.

예시:

```java
// DTO 정의
public class MemberDto {
    private String name;
    private String teamName;

    public MemberDto(Member member) {
        this.name = member.getName();
        this.teamName = member.getTeam().getName(); // Lazy 로딩 처리됨
    }
}

// 서비스 계층
public MemberDto getMember(Long id) {
    Member member = memberRepository.findById(id).orElseThrow();
    return new MemberDto(member); // DTO 변환
}

// 컨트롤러
@GetMapping("/member/{id}")
public MemberDto getMember(@PathVariable Long id) {
    return memberService.getMember(id); // 이미 DTO 상태
}
```

이러한 구조를 통해 컨트롤러는 순수하게 응답 포맷에 집중할 수 있으며, 트랜잭션 종료 후의 예외를 예방할 수 있습니다.
