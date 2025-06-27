# 트랜잭션 격리수준
동시에 여러 트랜잭션이 실행될 때 한 트랜잭션이 다른 트랜잭션의 연산에 영향을 받지 않도록 하는 정도를 말한다.
낮은 격리 수준은 동시 처리 능력을 높이지만, 데이터의 일관성 문제를 발생시킬 수 있다.
반면, 높은 격리 수준은 데이터의 일관성을 보장하지만, 동시 처리 능력이 떨어질 수 있다.
즉, 데이터 정합성과 성능은 반비례한다. 트랜잭션 격리 수준은 개발자가 트랜잭션 격리 수준을 설정할 수 있는 기능을 제공하는 기능이다.

---
✅ 면접에서는 이렇게 물어볼 수 있다:
- "트랜잭션 격리 수준마다 어떤 문제가 발생하나요?"
- "READ COMMITTED와 REPEATABLE READ의 차이는 무엇인가요?"
- "REPEATABLE READ에서도 Phantom Read가 발생하는 이유는 뭔가요?"

✅ 실무에서 고려할 점:
- 대부분의 RDBMS(MySQL 등)는 기본 격리 수준으로 READ COMMITTED 또는 REPEATABLE READ를 사용한다.
- 성능을 위해 READ COMMITTED를 쓰되, 반복 조회에서 일관성이 중요한 경우에는 REPEATABLE READ나 SERIALIZABLE을 고려한다.


✅ 트랜잭션 격리 수준 설정 예시 (Spring + JPA):
```java
@Transactional(isolation = Isolation.REPEATABLE_READ)
public void processOrder() {
    // 비즈니스 로직
}
```

```java
// ✅ READ COMMITTED 예시: Non-Repeatable Read 발생 가능
@Transactional(isolation = Isolation.READ_COMMITTED)
public void readCommittedExample() {
    int stock1 = inventoryRepository.findStockByProductId(1L); // 예: 100
    // 다른 트랜잭션이 해당 데이터를 50으로 수정하고 커밋
    int stock2 = inventoryRepository.findStockByProductId(1L); // 예: 50 (변경된 값 반영됨)
}

// ✅ REPEATABLE READ 예시: Non-Repeatable Read 방지
@Transactional(isolation = Isolation.REPEATABLE_READ)
public void repeatableReadExample() {
    int stock1 = inventoryRepository.findStockByProductId(1L); // 예: 100
    // 다른 트랜잭션이 데이터를 수정하더라도
    int stock2 = inventoryRepository.findStockByProductId(1L); // 여전히 100 (변경 내용 보이지 않음)
}
```

위 예제는 READ COMMITTED와 REPEATABLE READ의 차이를 보여준다.

READ COMMITTED에서는 커밋된 최신 데이터를 읽기 때문에, 동일한 쿼리를 실행하더라도 다른 결과를 받을 수 있다.
반면 REPEATABLE READ는 트랜잭션 시작 시점의 스냅샷을 기준으로 데이터를 조회하므로, 같은 쿼리를 반복해도 동일한 결과를 보장한다.
이는 REPEATABLE READ가 Non-Repeatable Read를 방지할 수 있게 해주는 핵심 동작이다.

✅ 정리표

| 격리 수준         | Dirty Read | Non-Repeatable Read | Phantom Read | 성능 |
|------------------|------------|----------------------|---------------|------|
| READ UNCOMMITTED | 발생       | 발생                 | 발생          | 👍👍👍👍 |
| READ COMMITTED   | X          | 발생                 | 발생          | 👍👍👍  |
| REPEATABLE READ  | X          | X                    | 발생          | 👍👍   |
| SERIALIZABLE     | X          | X                    | X             | 👍    |

## 트랜잭션 격리 수준은 어떤 것이 있고 각각 어떤 특징이 있나?
트랜잭션 격리 수준은 READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE 네 가지가 존재한다.

### READ UNCOMMITTED
커밋이 되지 않은 트랜잭션의 데이터 변경 내용을 다른 트랜잭션이 조회하는 것을 허용한다.
또한 해당 격리 수준에서는 Dirty Read, Phantom Read, Non-Repeatable Read 문제가 발생할 수 있다.

### READ COMMITTED
커밋이 완료된 트랜잭션의 변경사항만 다른 트랜잭션에서 조회할 수 있도록 허용한다.
트랜잭션이 이루어지는 동안, 다른 트랜잭션은 해당 데이터에 접근할 수 없다.
Dirty Read는 발생하지 않지만, Phantom Read, Non-Repeatable Read 문제가 발생할 수 있다.

### REPEATABLE READ
한 트랜잭션에서 특정 레코드를 조회할 때 항상 같은 데이터를 응답하는 것을 보장한다.
하지만, SERIALIZABLE과 다르게 행이 추가되는 것을 막지는 않는다.
Non-Repeatable Read 문제가 발생하지 않지만, Phantom Read 문제가 발생할 수 있다.

### SERIALIZABLE
특정 트랜잭션이 사용중인 테이블의 모든 행을 다른 트랜잭션이 접근할 수 없도록 잠근다.
가장 높은 데이터 정합성을 가지지만 성능이 가장 낮다. MySQL의 경우 단순 SELECT 쿼리가 실행되더라도 데이터베이스 잠금이 걸려 다른 트랜잭션에서 데이터에 접근할 수 없다.

## 발생 문제
### Dirty Read
한 트랜잭션이 변경 중인 데이터를 읽는 경우 발생한다.
다른 트랜잭션이 아직 커밋되지 않은(즉, 롤백할 가능성이 있는) 데이터를 읽어서, 그 데이터가 나중에 롤백될 경우 트랜잭션의 결과가 변경될 수 있다. 이는 데이터의 일관성을 깨뜨릴 수 있다.

### Phantom Read
한 트랜잭션이 동일한 쿼리를 두 번 실행했을 때, 두번의 쿼리 사이에 다른 트랜잭션이 삽입, 갱신, 삭제 등의 작업을 수행하여 결과 집합이 달라지는 경우를 말한다. 이로 인해 트랜잭션 내에서 일관성 없는 결과를 가져올 수 있다.

### Non-Repeatable Read
같은 트랜잭션 안에서 동일한 쿼리를 실행했을 때, 다른 결과를 얻는 경우 의미한다.
예를 들어, 한 트랜잭션이 같은 데이터를 두 번 읽을 때, 첫 번째 읽기와 두 번째 읽기 사이에 다른 트랜잭션이 해당 데이터를 변경했을 경우 발생할 수 있다.

---
💡 추가로 알아두면 좋은 개념: Snapshot Isolation
- 일부 DB (예: PostgreSQL)는 MVCC 기반의 Snapshot Isolation을 제공해 READ COMMITTED에서도 Phantom Read를 방지할 수 있다.
- 이 경우 REPEATABLE READ ≠ Snapshot Isolation임을 유의할 것.