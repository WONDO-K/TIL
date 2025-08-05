# SOLID 원칙
객체지향 설계 5원칙이라고도 불리며, 각 원칙의 앞 글자를 따서 만들어졌다.
객체지향 설계의 핵심 중 하나는 의존성을 관리하는 것이다. 의존성을 잘 관리하기 위해서는 SOLID 원칙을 준수해야 한다.

## Single Responsibility Principle (SRP) - 단일 책임 원칙
클래스가 오직 하나의 목적이나 이유로만 변경되어야 한다는 원칙이다.
여기서 "책임"이란 단순히 메서드의 갯수를 뜻하지 않고, 특정 사용자나 기능 요구사항에 따라 소프트웨어의 변경 요청을 처리하는 역할을 의미한다.
즉, 클래스는 한 가지 변화의 이유만 가져야 하며, 이를 통해 변경이 발생했을 때는 다른 기능에 영향이 덜 미치도록 설계하여 유지보수성을 높이고 코드의 가독성을 향상시킨다.

## Open/Closed Principle (OCP) - 개방/폐쇄 원칙
확장에는 열려있고, 변경에는 닫혀 있어야 한다는 원칙이다.
이때, 확장이란 새로운 타입을 추가함으로써 새로운 기능을 추가하는 것을 의마하며, 폐쇄란 확장이 일어날 때 상위 레벨의 모듈이 영향을 받지 않아야 함을 의미한다. 이를 통해서 모듈의 행동을 쉽게 변경할 수 있다. 모듈이란 크기와 상관없이 클래스, 패키지, 라이브러리와 같이 프로그램을 구성하는 임의의 요소를 의미한다.

## 예제

```java
// OCP 원칙을 적용한 예제: 주문 금액에 따라 다른 할인 정책 적용

class Order {
    private int amount;
    private DiscountPolicy discountPolicy;

    public Order(int amount, DiscountPolicy discountPolicy) {
        this.amount = amount;
        this.discountPolicy = discountPolicy;
    }

    public int calculateFinalPrice() {
        int discount = discountPolicy.getDiscount(amount);
        return amount - discount;
    }
}

public class Main {
    public static void main(String[] args) {
        // 고정 할인 정책 적용
        DiscountPolicy policy1 = new FixedDiscountPolicy();
        Order order1 = new Order(10000, policy1);
        System.out.println("최종 결제 금액 (고정 할인): " + order1.calculateFinalPrice());

        // 등급 할인 정책 적용
        DiscountPolicy policy2 = new GradeDiscountPolicy();
        Order order2 = new Order(10000, policy2);
        System.out.println("최종 결제 금액 (등급 할인): " + order2.calculateFinalPrice());
    }
}
```

- 이 코드는 `Order` 객체가 `DiscountPolicy` 인터페이스에만 의존하며, 새로운 정책을 추가할 때 기존 `Order` 코드는 변경하지 않음. OCP를 지킨 구조임.
```
## Liskov Substitution Principle (LSP) - 리스코프 치환 원칙
서브 타입은 언제나 상위 타입으로 교체할 수 있어야 한다. 즉, 서브 타입은 상위 타입이 약속한 규약을 지켜야 한다는 원칙이다. 이 원칙은 부모 쪽으로 업 캐스팅하는 것이 안전함을 보장하기 위해 존재한다. 만약 서브 타입이 상위 타입의 규약을 지키지 않는다면, 상위 타입을 사용하는 코드에서 서브 타입을 사용할 때 예기치 않은 동작이 발생할 수 있다.
이렇게 되면 상위 타입을 사용하는 클라이언트 코드에서는 하위 타입이 누구인지 물어봐야 하며, 이는 OCP를 달성하기 어렵게 만든다. LSP 위반의 대표적인 사례로는 Rectangle 예제가 있다.

## Interface Segregation Principle (ISP) - 인터페이스 분리 원칙
인터페이스는 그 인터페이스를 사용하는 클라이언트에 맞게 분리되어야 한다는 원칙이다. 즉, 클라이언트가 사용하지 않는 메서드를 포함하지 않아야 한다는 의미이다. 사용하지 않지만 의존성을 가지고 있다면 해당 인터페이스가 변경되는 경우 클라이언트 코드도 영향을 받게 된다. 따라서, 독립적인 개발과 배포가 불가능해진다.
사용하는 기능만 제공하도록 인터페이스를 분리함으로써, 클라이언트가 필요로 하는 기능만을 의존하게 하고, 변경에 대한 영향을 최소화할 수 있다.

## Dependency Inversion Principle (DIP) - 의존성 역전 원칙
고수준 모듈은 저수준 모듈에 의존해서는 안 되며, 둘 다 추상화에 의존해야 한다는 원칙이다. 즉, 고수준 모듈과 저수준 모듈 모두 인터페이스나 추상 클래스를 통해 의존성을 관리해야 한다는 의미이다. 이를 통해 고수준 모듈과 저수준 모듈 간의 결합도를 낮추고, 변경에 대한 유연성을 높일 수 있다.
의존성 역전 원칙을 통해서 하위 레벨의 모듈은 개방 폐쇄 원칙을 준수하면서 새로운 타입이 추가 가능하다.

## OCP는 앞으로 어떤 확장이 필요한지 알아야 준수할 수 있는 것 아닌가?
### 실무에서의 현실적인 적용
OCP를 철저히 지키기 위해서는 앞으로 일어날 모든 변경 가능성을 예측하고 확장 가능하도록 설계해야 하지만, 현실적으로는 불가능하거나 오버엔지니어링이 될 수 있다. 

따라서 실무에서는 "고객이 요청한 요구사항만 먼저 구현하고, 변경이 반복되는 시점에서 OCP 원칙에 맞춰 리팩토링하는 방식"이 자주 사용된다. 이러한 접근은 YAGNI(You Ain't Gonna Need It) 원칙과도 맞닿아 있으며, 유지보수성과 속도 사이의 균형을 맞추는 데 실용적이다.

예를 들어, 할인 정책을 처음에는 고정된 10% 할인으로 간단히 구현하고, 이후 등급별 할인, 시즌별 할인 등의 요구가 생기면 그때 인터페이스 기반으로 리팩토링하여 다양한 정책을 확장하는 방식이 현실적인 OCP 적용 사례이다.

### 예시 코드
```java
// 처음엔 이렇게 단순 구현 (고정 10% 할인)
class DiscountService {
    public int getDiscount(int price) {
        return price * 10 / 100; 
    }
}
```
> 고객이 등급별, 시즌별 할인을 요구함 -> 그때 OCP에 따라 인터페이스로 리팩토링
```java
// 인터페이스로 리팩토링 후 다양한 할인 정책 구현
interface DiscountPolicy {
    int getDiscount(int price);
}
class FixedDiscountPolicy implements DiscountPolicy {
    public int getDiscount(int price) {
        return price * 10 / 100;
    }
}
class GradeDiscountPolicy implements DiscountPolicy {
    public int getDiscount(int price) {
        // 등급별 할인 로직
    }
}
class SeasonalDiscountPolicy implements DiscountPolicy {
    public int getDiscount(int price) {
        // 시즌별 할인 로직
    }
}
```