package hello.core.singleton;

import hello.core.AppConfig;
import hello.core.member.MemberService;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class SingletonTest {
    
    @Test
    @DisplayName("스프링 없는 순수한 DI 컨테이너")
    void pureContatiner(){
        AppConfig appConfig = new AppConfig();
        // 1. 조회 : 호출할 때 마다 객체 생성
        MemberService memberService1 = appConfig.memberService();

        // 2. 조회 : 호출할 때 마다 객체 생성
        MemberService memberService2 = appConfig.memberService();

        // 참조값이 다른 것을 확인
        System.out.println("memberService1 = " + memberService1);
        System.out.println("memberService2 = " + memberService2);

        // memberService1 != memberService2
        // 사실 memberService만 생성하는 것이 아니라 MemberServiceImpl이 파라미터로 가지는 memberRepository도 생성하게 된다.
        // 즉, 총 4개의 객체가 실행시 생성된다는 것이다.
        Assertions.assertThat(memberService1).isNotEqualTo(memberService2);
    }
}
