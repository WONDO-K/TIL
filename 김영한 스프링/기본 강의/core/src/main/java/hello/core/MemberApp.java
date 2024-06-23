package hello.core;

import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MemberApp {

    public static void main(String[] args) {
        
//        AppConfig appConfig = new AppConfig();
//        MemberService memberService = appConfig.memberService();

        // 스프링은 모든 것이 ApplicationContext를 통해 실행된다.
        // AppConfig에 있는 환경 설정 정보를 토대로 객체생성해서 스프링 컨터이너에 빈들을 담아 놓는다.
        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);// 컨테이너에서 memberService를 찾아서 꺼낼 건데 타입은 MemberService

        Member member = new Member(1L, "memberA", Grade.VIP); // id를 Long 타입으로 지정했기 때문에 1L
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("newMember = " + member.getName());
        System.out.println("findMember = " + findMember.getName());
    }
}
