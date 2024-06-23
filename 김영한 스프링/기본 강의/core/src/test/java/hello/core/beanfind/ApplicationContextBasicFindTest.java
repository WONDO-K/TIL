package hello.core.beanfind;

import hello.core.AppConfig;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertThrows;

class ApplicationContextBasicFindTest {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
    
    @Test
    @DisplayName("빈 이름으로 조회")
    void findBeanByName(){
        // MemberService(인터페이스로 조회) -> 인터페이스의 구현체가 대상이 된다.
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);

    }

    @Test
    @DisplayName("빈 이름없이 타입으로 조회")
    void findBeanByType(){
        MemberService memberService = ac.getBean(MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);

    }

    @Test
    @DisplayName("구체 타입으로 조회")
    void findBeanByName2(){
        // MemberService(인터페이스로 조회) -> 인터페이스의 구현체가 대상이 된다.
        MemberServiceImpl memberService = ac.getBean("memberService", MemberServiceImpl.class);
        // MemberService 타입이 아니어도 상관없다. -> 스프링 빈에 등록된 인스턴스 타입을 보고 결정
        // (AppConfig 참고) MemberService는 MemberServiceImpl 인스턴스를 리턴한다.
        // 구체적인 타입을 적는 것은 역할에 집중하는 것이 아닌 구현에 집중하기 때문에 좋지 않다.
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);

    }

    @Test
    @DisplayName("빈 이름으로 조회 x")
    void findBeanByNameX(){
        // ac.getbean("xxxx", MemberService.class);
        // 람다식이 실행되면 NoSuchBeanDefinitionException 예외가 발생해야 한다는 의미
        // 예외가 안터지면 실패, 터지면 성공
        assertThrows(NoSuchBeanDefinitionException.class,
                ()-> ac.getBean("xxxxx", MemberService.class));
    }

}
