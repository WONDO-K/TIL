# equals와 hashCode는 왜 함께 재정의 하는가?
equals와 hashCode 메서드는 객체의 동등성 비교와 해시값 생성을 위해서 사용할 수 있다.
하지만, 함께 재정의하지 않는다면 예상치 못한 결과를 만들수 있다.
가령, 해시값을 사용하는 구조(HashSet, HashMap..)을 사용할 때 문제가 발생할 수 있다.

```java
class EqualsHashCodeTest {

    @Test
    @DisplayName("equals만 정의하면 HashSet이 제대로 동작하지 않는다.")
    void test() {
        // 아래 2개는 같은 구독자
        Subscribe subscribe1 = new Subscribe("team.maeilmail@gmail.com", "backend");
        Subscribe subscribe2 = new Subscribe("team.maeilmail@gmail.com", "backend");
        HashSet<Subscribe> subscribes = new HashSet<>(List.of(subscribe1, subscribe2));

        // 결과는 1개여야 한다. 왜냐하면 subscribe1과 subscribe2는 논리적으로 같은 값이지만,
        // hashCode()를 재정의하지 않으면 서로 다른 해시 버킷에 들어가므로 중복으로 간주되지 않는다.
        System.out.println(subscribes.size());
    }

    class Subscribe {

        private final String email;
        private final String category;

        public Subscribe(String email, String category) {
            this.email = email;
            this.category = category;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Subscribe subscribe = (Subscribe) o;
            return Objects.equals(email, subscribe.email) && Objects.equals(category, subscribe.category);
        }
    }
}
```

## 왜 이런 현상이 발생하는가?

`HashSet`, `HashMap`과 같은 해시 기반 자료구조는 내부적으로 `hashCode()`의 반환값을 기반으로 데이터를 저장할 위치(버킷)를 결정한다.

그런데 `hashCode()`를 따로 재정의하지 않으면, Java는 `Object` 클래스의 기본 구현을 사용한다. 이 기본 구현은 객체의 **메모리 주소를 기반으로** 해시값을 생성하기 때문에, 아무리 내용이 같아도 **서로 다른 객체는 서로 다른 해시값**을 갖게 된다.

따라서 다음과 같은 일이 벌어진다:

- `subscribe1`과 `subscribe2`는 논리적으로는 같은 값이지만
- 서로 다른 해시값을 가지므로 HashSet은 **서로 다른 객체**로 간주하고
- 결과적으로 **중복 제거가 되지 않는다**

## 왜 hashCode만으로는 중복 제거가 안 되는가?

HashSet이나 HashMap은 내부적으로 다음 2단계를 거친다:

1. `hashCode()`로 버킷을 선택
2. 버킷 안에서 `equals()`로 실제로 같은 객체인지 비교

따라서 다음과 같은 규칙이 성립한다:
- `hashCode()`가 같으면 같은 버킷에 저장된다.
- `equals()`가 true여야 비로소 동일한 객체로 간주되어 중복이 제거된다.

즉, `hashCode()`가 같다고 해서 무조건 같은 객체로 간주되는 것이 아니며, `equals()`까지 같아야 완전히 중복으로 판단된다.

## 올바른 equals와 hashCode 정의 예시

아래는 equals와 hashCode를 함께 정의하여 HashSet이 중복을 잘 처리하도록 만든 예시이다:

```java
class EqualsHashCodeTest {

    @Test
    @DisplayName("equals와 hashCode를 모두 정의하면 HashSet이 정상 동작한다.")
    void test() {
        Subscribe subscribe1 = new Subscribe("team.maeilmail@gmail.com", "backend");
        Subscribe subscribe2 = new Subscribe("team.maeilmail@gmail.com", "backend");

        HashSet<Subscribe> subscribes = new HashSet<>(List.of(subscribe1, subscribe2));
        System.out.println(subscribes.size()); // ✅ 1 출력
    }

    static class Subscribe {

        private final String email;
        private final String category;

        public Subscribe(String email, String category) {
            this.email = email;
            this.category = category;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Subscribe that = (Subscribe) o;
            return Objects.equals(email, that.email) &&
                   Objects.equals(category, that.category);
        }

        @Override
        public int hashCode() { // 주어진 필드들의 값을 바탕으로 객체의 해시코드를 생성한다.
            return Objects.hash(email, category);
        }
    }
}
```
### hashCode 동작 과정
1.	email, category 값들을 인자로 받아
2.	내부적으로 Arrays.hashCode(Object[])를 호출해
3.	null-safe하며 일관된 해시값을 생성한다.


### 정리

| 항목 | 설명 |
|------|------|
| `equals()` | 두 객체가 논리적으로 동일한지 비교 |
| `hashCode()` | 객체의 해시값. HashMap, HashSet에서 버킷 분배 기준 |
| 핵심 원칙 | equals가 같으면 hashCode도 같아야 함 |

### 추가 팁: `@EqualsAndHashCode`(Lombok)

lombok의 `@EqualsAndHashCode`를 클래스 위에 붙이면 equals와 hashCode를 자동 생성할 수 있다.

```java
@EqualsAndHashCode
public class Subscribe {
    private final String email;
    private final String category;
}
```