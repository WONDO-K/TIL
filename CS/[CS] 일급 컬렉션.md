# 일급 컬렉션(First-Class Collection)
하나의 컬렉션을 감싸는 클래스를 만들고, 해당 클래스에서 컬렉션과 관련된 비즈니스 로직을 관리하는 패턴을 말한다.
## Order의 List 자료구조를 감싼 Orders 일급 컬렉션 예시
```java
// 일급 컬렉션
public class Orders {

    private final List<Order> orders;

    public Orders(List<Order> orders) {
        validate(orders); // 검증 수행
        ...
    }

    public void add(Order order) {
        if (order == null) {
            throw new IllegalArgumentException("Order cannot be null");
        }
        orders.add(order);
    }

    public List<Order> getAll() {
        return Collections.unmodifiableList(orders);
    }

    public double getTotalAmount() {
        return orders.stream()
                     .mapToDouble(Order::getAmount)
                     .sum();
    }
}

```
```java
public class OrderService {
  
    private final Orders orders = new Orders();

    public void addOrder(Order order) {
        orders.add(order);
    }

    public Orders getOrders() {
        return orders;
    }

    // 추가 비즈니스 로직...
}
```

## 일급 컬렉션을 사용해야하는 이유는 무엇인가?
일급 컬렉션 클래스에 로직을 포함하거나 비즈니스에 특화된 명확한 이름을 부여할 수 있다.
또한, 불필요한 컬렉션 API를 외부로 노출하지 않도록 할 수 있으며, 컬렉션을 변경할 수 없도록 만든다면 예기치 않은 변경으로부터 데이터를 보호할 수 있다.

---

## 실무에서 일급 컬렉션을 어떻게 사용하는가?

보통은 Repository에서 쿼리를 통해 `List<Order>` 형태의 데이터를 바로 받아와 Service나 Controller에서 비즈니스 로직을 처리하는 경우가 많다.

```java
// 일반적인 방식 (일급 컬렉션 미사용)
List<Order> orders = orderRepository.findByUserId(userId);
double total = orders.stream().mapToDouble(Order::getAmount).sum();
```

### 단점
- 도메인 로직이 서비스/컨트롤러에 흩어짐
- 유효성 검증, 필터링, 합산 등을 매번 반복해야 함

---

## ✅ 일급 컬렉션 방식

```java
List<Order> orderList = orderRepository.findByUserId(userId);
Orders orders = new Orders(orderList); // 감싸기!

double total = orders.getTotalAmount(); // 내부에서 비즈니스 로직 처리
```

### 장점
- Orders 객체 내부에 검증, 계산, 정렬 등 도메인 로직을 캡슐화 가능
- 서비스/컨트롤러에서는 "의미 있는 객체"로 다룰 수 있음

---

## 🔧 실무 예시

```java
// Repository
List<Order> orderList = orderRepository.findByUserId(userId);

// Service
Orders orders = new Orders(orderList);
return orders.getCompletedOrders(); // 내부에서 비즈니스 로직 처리
```

- `getCompletedOrders()` 같은 메서드는 Orders 내부에서 처리됨
- 비즈니스 규칙은 오직 Orders 안에서 관리됨

---

## 🔍 왜 굳이 감싸는가?

| 이유            | 설명                                                        |
|-----------------|-------------------------------------------------------------|
| 응집도 향상      | 로직이 분산되지 않고 Orders 내부에 모임                      |
| 컬렉션 보호      | 불변 컬렉션으로 외부 수정 차단 가능                          |
| 의미 전달        | `List<Order>`보다 `Orders`가 더 명확한 의미 전달            |
| 테스트 용이성     | 검증/로직 단위 테스트가 쉬워짐                               |

---

## 💬 면접에서는 이렇게 질문될 수 있어요:

**“List 대신 굳이 Orders로 감싸는 이유는 뭔가요?”**  
→ "비즈니스 규칙을 서비스 레이어가 아니라 도메인 객체에서 처리하게 해 응집도를 높이고, 컬렉션을 불변으로 만들어 실수로 데이터가 변경되는 걸 방지할 수 있기 때문입니다."