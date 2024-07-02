package hello.core;

import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;

@Configuration
@ComponentScan(
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Configuration.class) // 컴포넌트 스캔에서 제외할 항목
        // AppConfig의 @Configuration은 수동을 등록하기 때문에 자동으로 등록해버리면 안된다. 그리고 원래 @Component가 붙어 있어서 스캔 대상임
) // @ComponentScan는 스프링 빈을 자동으로 끌어올려야함, @Component 어노테이션이 붙어 있는 클래스를 찾아서 자동으로 스프링 빈에 등록해준다.
public class AutoAppConfig {

    @Bean(name="memoryMemberRepository")
    MemberRepository memberRepository(){
        return new MemoryMemberRepository();
    }

}
