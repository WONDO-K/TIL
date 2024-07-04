package hello.core;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import hello.core.member.MemoryMemberRepository;
import hello.core.order.OrderService;
import hello.core.order.OrderServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration //AppConfig에 설정을 구성한다는 뜻의 @Configuration 을 붙여준다.
public class AppConfig { // AppConfig가 의존관계를 대신 주입하기 때문에 DI 컨테이너임

    // @Bean -> memberService -> new MemoryMemberRepository
    // @Bean -> orderSerivce -> new MemoryMemberRepository
    // 2번 호출이 된다.

    // 순서는 보장되지 않는다. memberRepository가 3번 호출되는 것이 예상
    // call AppConfig.memberService
    // call AppConfig.memberRepository
    // call AppConfig.memberRepository
    // call AppConfig.orderService
    // call AppConfig.memberRepository

    // 실제
    // call AppConfig.memberService
    // call AppConfig.memberRepository
    // call AppConfig.orderService

    @Bean // 각 메서드에 @Bean 을 붙여준다. 이렇게 하면 스프링 컨테이너에 스프링 빈으로 등록한다
    public MemberService memberService(){
        System.out.println("call AppConfig.memberService");
        return new MemberServiceImpl(memberRepository());
    }
    @Bean
    public MemoryMemberRepository memberRepository() {
        System.out.println("call AppConfig.memberRepository");
        return new MemoryMemberRepository();
    }
    @Bean
    public OrderService orderService(){
        System.out.println("call AppConfig.orderService");
         return new OrderServiceImpl(memberRepository(), discountPolicy());
        // return null;
    }
    @Bean
    public DiscountPolicy discountPolicy(){
        // return new FIxDiscountPolicy();
        return new RateDiscountPolicy();
    }
}
