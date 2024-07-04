package hello.core.autowired;

import hello.core.member.Member;
import jakarta.annotation.Nullable;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.util.Optional;

public class AutowiredTest {

    @Test
    void AutowiredOption(){
        ApplicationContext ac = new AnnotationConfigApplicationContext(TestBean.class); // TestBean가 스프링 빈으로 등록된다.

    }

    static class TestBean{

        @Autowired(required = false) // 의존관계가 없으면 해당 메서드 호출 자체를 하지 않는다.
        public void setNoBean1(Member noBean1){ //Member는 순수 자바코드로 스프링이 관리 하지 않는다. -> 스프링에서 관리하는 빈이 없는 상태
            System.out.println("noBean1 = " + noBean1);
        }

        @Autowired
        public void setNoBean2(@Nullable Member noBean2){ //Member는 순수 자바코드로 스프링이 관리 하지 않는다. -> 스프링에서 관리하는 빈이 없는 상태
            System.out.println("noBean2 = " + noBean2);
        }

        @Autowired
        public void setNoBean3(Optional<Member> noBean3){
            System.out.println("noBean3 = " + noBean3);
        }
    }

}
