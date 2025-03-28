# Object타입인 Value 타입 변환
## String으로 타입 캐스팅 과 String.valueOf()의 차이점
두 방식 모두 String 타입으로 변환하는 것은 동일하지만, 동작 방식과 예외 처리에서 차이가 발생한다.

- (String) value 로 타입 캐스팅 하는 것은 value가 String 타입이 아닌 경우 ClassCastException이 발생하며, value가 null인 경우 그대로 null을 반환하여 이후 메서드를 호출할 떄 NullPointerException이 발생한다.
조금 쉽게 이해하자면 형변환은 개발자가 이 Object가 실제로 해당 타입(여기서는 String)이라고 확신한다는 전제하에 컴파일러에게 그렇게 취급하라고 지시하는 것 -> 캐스팅을 한다고 실제 객체의 타입이 바뀌지는 않는다 그저 참조 방식을 바꾸는 것일 뿐
타입 캐스팅은 타입 안정성이 부족하기 떄문에 캐스팅하는 타입이 확실할 때만 사용해야 한다.
```java
Object intValue = 10;
String str1 = (String) intValue; // ClassCastException

Object nullValue = null;
String str2 = (String) nullValue; // null
str2.concat("maeilmail"); // NullPointerException
```

- String.valueOf(value)는 value가 String 타입이 아닌 경우 value.toString()을 호출하여 String으로 변환하며, value가 null인 경우 "null" 문자열을 반환한다.

```java
Object intValue = 10;
String str1 = String.valueOf(intValue); // "10"

Object nullValue = null;
String str2 = String.valueOf(nullValue); // "null"
str2.concat("maeilmail"); // "nullmaeilmail"
```
- 타입 캐스팅에서 발생하는 예외는 런타임 시점에 발생하기 떄문에 String.valueOf()가 더 안전하고 예외를 방지할 수 있다.

## 타입 캐스팅을 할 때 ClassCastException을 방지하는 방법은 무엇이 있을까?
캐스팅할 타입과 맞는지 먼저 확인 후 캐스팅하면 ClassCastException을 방지할 수 있다.
이때, instanceOf를 사용하면 안전하게 변환할 수 있다.
```java
Object intValue = 10;

if (intValue instanceof String str) { // intValue가 String으로 선언되었는지 확인
    System.out.println(str);
} else {
    // ...
}
```

## String.valueOf(null)이 null을 반환하는 것에 대한 문제
"null"이라는 문자열과 null 자체는 다른 의미를 가질 수 있기 떄문에 문제가 될 수 있다.
특히, Json 변환이나 데이터베이스에 저장할 때 null이 "null"로 저장되어 오류가 발생할 수도 있다.
원치 않게 null이 문자열로 저장되는 것을 방지하려면 미리 null 여부를 검증하고 따로 처리하거나
Objects.toString()을 사용하여 null일 경우 다른 문자열로 처리하는 방법 사용