# 동일성과 동등성
자바에서는 이 두 개념을 equals() 메서드와 == 연산자를 통해 구분할 수 있다.
equals()와 ==의 차이는 무엇인가?
- equals() : 객체의 내용을 비교
- == : 객체의 참조(레퍼런스)를 비교한다.
따라서 두 객체의 내용이 같더라도 서로 다른 객체라면 equals()는 true 반환할 수 있지만, ==는 false를 반환한다.

## 동등성(Equality)는 무엇인가?
동등성은 논리적으로 객체의 내용이 같은지를 비교하는 개념이다.
자바에서는 equals() 메서드를 사용하여 객체의 동등성을 비교한다.
아래의 Apple 클래스 예제를 보면, Object.equals 메서드를 오버라이딩하여 객체의 실제 데이터를 비교하도록 했다.
그래서 apple과 anotherApple은 다른 객체이지만, 무게가 같기 때문에 동등성 비교 결과 true가 반환된다.

```java
public class Apple {

    private final int weight;

    public Apple(int weight) {    
        this.weight = weight;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Apple apple = (Apple) o;
        return weight == apple.weight;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(weight);
    }

    public static void main(String[] args) {
        Apple apple = new Apple(100);
        Apple anotherApple = new Apple(100);

        System.out.println(apple.equals(anotherApple)); // true
    }
}
```

## 왜 equals()를 오버라이딩 하는가?
```java
public class Apple {

    private final int weight;

    public Apple(int weight) {
        this.weight = weight;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Apple apple = (Apple) o;
        return weight == apple.weight;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(weight);
    }

    public static void main(String[] args) {
        Apple apple = new Apple(100);
        Apple anotherApple = new Apple(100);

        System.out.println(apple.equals(anotherApple)); // true
    }
}
```
Object 클래스의 equals() 메서드는 == 연산자를 사용하여 동일성을 비교한다.
그리고 모든 클래스는 Object 클래스를 상속하여 동일성 비교를 기본으로 동작하기 때문에, 
동등성 비교가 필요한 클래스에 맞게 equals & hashCode 메서드를 오버라이딩 해야한다.

## 동일성(Identity)
동일성은 두 객체가 메모리 상에서 같은 객체인지 비교하는 개념이다.
자바에서는 "==" 연산자를 사용하여 객체의 동일성을 비교한다.
"==" 연산자는 객체의 레퍼런스(참조)를 비교하므로, 두 변수가 동일한 객체를 가리키고 있는지를 확인한다.

```java
public static void main(String[] args) {
    Apple apple1 = new Apple(100);
    Apple apple2 = new Apple(100);
    Apple apple3 = apple1;

    System.out.println(apple1 == apple2); // false
    System.out.println(apple1 == apple3); // true
}
```
apple1과 apple2는 참조가 다르기 때문에 == 연산 결과 false가 반환되지만, apple1의 참조를 가지는 apple3은 "==" 연산 결과 true를 반환한다.

## String은 객체인데 == 비교해도 가능한데 무슨 차이인가?
문자열 리터럴은 문자열 상수 폴(String Constant Pool)에 저장되기 때문에, 동일한 문자열 리터럴을 참조하면 == 연선자가 true를 반환할 수 있다. 하지만 new 키워드를 사용하여 문자열을 생성하면 새로운 객체가 생성되므로 == 연산자가 false를 반환할 수 있다.
따라서 문자열 비교 시 항상 equals() 메서드를 사용한 동등성 비교를 하는 것이 좋다.
```java
public class StringComparison {
    public static void main(String[] args) {
        String str1 = "안녕하세요";
        String str2 = "안녕하세요";
        String str3 = new String("안녕하세요");
        
        // 동일성 비교
        System.out.println(str1 == str2); // true
        System.out.println(str1 == str3); // false
        
        // 동등성 비교
        System.out.println(str1.equals(str2)); // true
        System.out.println(str1.equals(str3)); // true
    }
}

// String.class equals 오버라이딩 되어있음.
public boolean equals(Object anObject) {
    if (this == anObject) {
        return true;
    }
    return (anObject instanceof String aString)
            && (!COMPACT_STRINGS || this.coder == aString.coder)
            && StringLatin1.equals(value, aString.value);
}
```

## Integer 같은 래퍼 클래스는 어떻게 비교하는가?

래퍼 클래스도 결국 객체(Object)이다. 자바에서 Integer, Double, Long 등은 원시 타입(int, double 등)을 감싸는 클래스이며, 메모리 상의 참조(주소값)를 가진다.

### 1. == 연산자: 참조(주소) 비교
- == 연산자는 값이 아닌 객체의 참조(주소)를 비교한다.
- 같은 값을 가진 Integer라도 new 키워드를 사용해 객체를 생성하면 서로 다른 객체가 되어 == 비교 시 false를 반환한다.

```java
Integer i1 = new Integer(100);
Integer i2 = new Integer(100);

System.out.println(i1 == i2); // false (서로 다른 객체)
```

### 2. equals() 메서드: 값 비교
- equals()는 객체 안의 실제 값을 비교한다.
- 값이 같으면 true를 반환한다.

```java
Integer i1 = new Integer(100);
Integer i2 = new Integer(100);

System.out.println(i1.equals(i2)); // true (값 비교)
```

### 3. 캐싱 범위 (-128 ~ 127)
- 자바는 Integer 캐싱을 통해 -128 ~ 127 범위의 숫자는 동일한 객체로 재사용한다.
- 이 범위 내에서는 == 비교도 true를 반환할 수 있다.

```java
Integer a = 100;
Integer b = 100;

System.out.println(a == b); // true (캐싱 적용)

Integer c = 200;
Integer d = 200;

System.out.println(c == d); // false (캐싱 적용 안 됨)
System.out.println(c.equals(d)); // true (값 비교)
```

### 4. 결론 및 권장 사항

| 비교 방법 | 설명 | 권장 여부 |
|----------|------|---------|
| `==` | 참조(주소) 비교 | ❌ 사용 지양 |
| `.equals()` | 값 비교 | ✅ 항상 사용 |

항상 equals()를 사용하는 습관이 안전하다. ==는 캐싱 범위, 객체 생성 방식에 따라 결과가 달라질 수 있어 신뢰할 수 없다.

## 알고리즘에서는 왜 `==`를 주로 사용하는가?

### 1. 기본 타입(primitive type) 중심
- 알고리즘 문제에서는 속도와 효율성이 중요하기 때문에 int, long, char, boolean 같은 기본형 타입을 주로 사용한다.
- 기본형은 `==` 연산자를 사용하여 값 자체를 비교한다.
```java
int a = 5;
int b = 5;
System.out.println(a == b); // true
```

### 2. 객체 비교가 드문 환경
- 알고리즘 문제에서는 대부분 값 비교에 초점이 맞춰져 있고, 복잡한 객체 비교가 드물다.
- 따라서 equals() 대신 `==`만으로 충분히 문제를 해결할 수 있다.

---

## 언제 equals()가 필요한가?

- 문자열(String) 비교
- 사용자 정의 객체 비교
- 래퍼 클래스 비교 (예: Integer, Long)

```java
String s1 = "abc";
String s2 = new String("abc");

System.out.println(s1 == s2); // false
System.out.println(s1.equals(s2)); // true
```

---

## 정리

| 상황 | 비교 방법 |
|------|----------|
| int, long, char 등 기본형 | `==` 사용 |
| String, 사용자 정의 객체 | `.equals()` 사용 |

- 알고리즘: 기본형 → `==`
- 실무: 참조형 → `.equals()`

항상 비교 대상의 타입과 목적에 맞게 선택해야 한다.