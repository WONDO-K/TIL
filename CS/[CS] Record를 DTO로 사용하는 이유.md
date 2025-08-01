# Record를 DTO로 사용하는 이유
Record는 Java 16에서 도입된 특별 유형의 클래스로 불변성(Immutable)을 기본으로 제공한다.
기존 클래스와 달리 모든 필드가 final로 선언되며, 객체 생성 후에는 변경할 수 없다.
또한 필드 선언만으로 자동으로 생성자, getter, equals(), hashCode(), toString() 메서드등을 자동으로 생성해주어 보일러 플레이트 코드를 줄일 수 있다. (보일러 플레이트 코드: 반복적으로 작성해야 하는 코드)
이러한 특성으로 인해 멀티 스레드 환경에서 데이터가 의도치 않게 변경되지 않고 안전하게 전달할 수 있다.

```java
// 기존 클래스 기반 DTO
public class MemberDto {

	private final String name;
	private final String email;
	private final int age;

	public MemberDto(String name, String email, int age) {
		this.name = name;
		this.email = email;
		this.age = age;
	}

	public String getName() {
		return name;
	}
	
	public String getEamil() {
		return email;
	}
	
	public int getAge() {
		return age;
	}
}
```
```java
// Record 기반 DTO
// 생성자, getter, equals(), hashCode(), toString() 메서드가 자동으로 생성됨
public record MemberDto(String name, String email, int age) {
}

## 그럼 Record로 생성한 모든 객체는 DTO인가?
모든 Record 객체가 DTO(Data Transfer Object)는 아니다.
Record는 단순히 데이터를 캡슐화하는 역할을 하는데, DTO 외에도 값 객체(Value Object)등의 다양한 용도로 사용될 수 있다.
```java
// 값 객체로 사용되는 Record
public record Coordinates(double x, double y) {
}
```
DTO는 계층 간 데이터 전송을 목적으로 하는 객체인 반면, VO는 도메인 모델 내에서 특정 값을 표현하는 객체로 사용된다.
따라서, Record는 이 두가지 모두에 적합하게 사용할 수 있지만, 그 목적에 따라 사용법이 달라진다.

## Record와 VO를 비교해주세요.
Record와 VO(Value Object)는 모두 객체의 상태가 변경되지 않는 것을 보장한다. 또 데이터를 캡슐화하여 표현하는 데 초점을 맞춘다. 마지막으로 VO는 값 기반의 동등성을 가지며, Record도 동일한 필드 값을 가지면 동일한 객체로 간주된다는 점이 공통점이다.

VO는 도메인 모델내에서 특정 개념을 표현하고, 도메인 로직과 밀접하게 관련이 있다. 즉, VO는 비즈니스 로직이나 규칙을 가질 수 있다. 반면에 Record는 단순히 데이터를 캡슐화하여 전달하는데 의미가 있다.

결론적으로 Record는 VO를 구현하는 데 적합하지만, VO의 모든 특성을 완벽히 대체하지 않는다. VO는 더 넓은 도메인 맥락에서 사용되며, 비즈니스 로직을 포함할 수 있다.

## Record의 한계는 무엇인가?
Record는 extends를 사용하여 다른 클래스를 상속할 수 없고, 필드가 final로 선언되기 때문에 확장이 어렵다.
또 주로 데이터를 전달하려는 목적으로 설계되었기 때문에 비즈니스 로직을 포함하기에 적절하지 않는다.
Java 14 또는 16 이전 버전에는 호환이 불가능하다.