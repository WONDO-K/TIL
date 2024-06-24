package hello.core.singleton;

public class SingletonService {

    // 클래스 레벨에 올라가기 때문에 하나만 존재하게 된다.
    private static final SingletonService instance = new SingletonService();

    public static SingletonService getInstance(){
        return instance;
    }

    private SingletonService(){ // private로 외부에서 객체를 새로 생성하는 경우를 차단한다.

    }
    
    public void logic(){
        System.out.println("싱글톤 객체 로직 호출");
    }

}
