# 템플릿 메서드 패턴
- 기능의 뼈대와 구현을 분리하는 행위 디자인 패턴이다.
- 템플릿 메서드 패턴은 실행 단계의 절차를 결정하는 상위 클래스와 실행 단계를 구현하는 하위 클래스로 구성된다.

```java
public abstract class Student {
  
    public abstract void study();
    public abstract void watchYoutube();
    public abstract void sleep();

    // 템플릿 메서드
    final public void doDailyRoutine() {
       study();
       watchYoutube();
       sleep();
    }
}

class BackendStuduent extends Student {

    @Override
    public void study() {
        System.out.println("영한님 JPA 강의를 수강합니다.");
    }

    @Override
    public void watchYoutube() {
        System.out.println("개발바닥 유튜브를 시청합니다.");   
    }

    @Override
    public void sleep() {
        System.out.println("7시간 잠을 잡니다.");   
    }
}
```

템플릿 메서드 패턴은 공통 로직을 상위 클래스에 모아 중복 코드를 줄일 수 있으며, 코드의 재사용성을 높일 수 있다는 장점이 있다.
하지만, 하위 클래스를 개발할 때 상위 클래스의 내용을 알기 전까지 어떠한 방식으로 동작할지 예측하기 어렵고, 상위 클래스 수정이 발생하는 경우 모든 하위 클래스를 변경해야 하는 단점이 존재한다. 

## 상위 클래스 수정 -> 모든 하위 클래스 변경해야하는 단점.
이는 상위 추상 클래스는 해당 클래스가 특정한 메서드가 필요하다고 상속 받는 하위 클래스들에게 메서드 구현을 강제하는 기능이기 때문에 변경해야한다 -> 즉, 상위 클래스에 메서드 추가되면 하위 클래스들은 그 메서드를 모두 구현해야함을 의미함.