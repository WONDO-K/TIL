## ✅ 낙관적 락 (Optimistic Lock)

낙관적 락은 데이터 충돌 가능성이 낮다고 보고, 먼저 데이터를 읽고, 변경 후 저장 시점에 다른 트랜잭션의 수정 여부를 검사하여 충돌을 방지하는 전략이다. 주로 **읽기 중심의 시스템**이나, **충돌 가능성이 낮은 업무 로직**에서 활용된다.

- 충돌 감지는 `@Version` 필드를 통해 수행
- 트랜잭션 격리 수준은 기본(Read Committed)이어도 무방
- 충돌 발생 시 `OptimisticLockingFailureException` 등의 예외 발생

### 🔸 예제

```java
@Entity
public class Product {
    @Id @GeneratedValue
    private Long id;

    private int stock;

    @Version
    private Long version;

    public void decreaseStock(int quantity) {
        if (stock < quantity) throw new IllegalStateException("재고 부족");
        this.stock -= quantity;
    }
}
```

```java
@Transactional
public void order(Long productId, int quantity) {
    Product product = productRepository.findById(productId).orElseThrow();
    product.decreaseStock(quantity); // 재고 감소
}
```

---

## ✅ 비관적 락 (Pessimistic Lock)

비관적 락은 충돌 가능성이 높다고 판단하고, 데이터를 읽는 순간부터 데이터에 락을 걸어 다른 트랜잭션의 접근을 차단한다. 주로 **재고 감소, 중복 주문 방지**처럼 **데이터 무결성이 매우 중요한 경우** 사용된다.

- `@Lock(LockModeType.PESSIMISTIC_WRITE)` 사용
- DB 레벨에서 행에 락을 건다 (예: `SELECT ... FOR UPDATE`)
- 성능 이슈가 있을 수 있음 (대기, 데드락 등)

### 🔸 예제

```java
@Lock(LockModeType.PESSIMISTIC_WRITE)
@Query("SELECT p FROM Product p WHERE p.id = :id")
Optional<Product> findByIdForUpdate(@Param("id") Long id);

@Transactional
public void order(Long productId, int quantity) {
    Product product = productRepository.findByIdForUpdate(productId).orElseThrow();
    product.decreaseStock(quantity); // 락 보장된 상태에서 재고 감소
}
```

---

## 🧠 실제 서비스에서는 어떻게 해야 하나요?

재고가 **자주 변경되거나 중요한 자원**이라면:

- **낙관적 락**으로 우선 처리 → 실패 시 예외 캐치 후 재시도 또는 사용자에게 알림
- **특정 상황에서만 비관적 락**을 제한적으로 도입 → 데드락 방지, 성능 확보

```java
@Transactional
public void order(Long productId, int quantity) {
    try {
        Product product = productRepository.findById(productId).orElseThrow();
        product.decreaseStock(quantity);
    } catch (OptimisticLockException e) {
        // 실패 시 비관적 락으로 재시도
        Product product = productRepository.findByIdForUpdate(productId).orElseThrow();
        product.decreaseStock(quantity);
    }
}
```

이처럼 **낙관적 락을 기본으로 사용하고, 충돌 발생 시 비관적 락으로 재처리하는 전략**이 실무에서 자주 사용된다.

## 참고 블로그
https://seungjjun.tistory.com/332#Case%204%20(%EB%8F%99%EC%8B%9C%EC%97%90%20%EC%97%AC%EB%9F%AC%20%EC%82%AC%EC%9A%A9%EC%9E%90%EA%B0%80%20%EB%8F%99%EC%9D%BC%20%EC%83%81%ED%92%88%20%EC%A3%BC%EB%AC%B8%20%EC%8B%9C%20%EC%9E%AC%EA%B3%A0%20%EC%B0%A8%EA%B0%90%20%EB%AC%B8%EC%A0%9C)-1-4