package hello.hello_spring.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Controller;

@Aspect
@Controller // 원래는 SpringConfig에 빈 등록을 하고 사용한다 (AOP가 사용되는 것을 인지하기위해)
public class TimeTraceAop {

    @Around("execution(* hello.hello_spring..*(..))") // 최상위 패키지 하위에 모두 적용
    public Object excute(ProceedingJoinPoint joinPoint) throws Throwable {

        long start = System.currentTimeMillis();
        System.out.println("START : " + joinPoint.toString());

        try {
            return joinPoint.proceed();
        } finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;
            System.out.println("END : " + joinPoint.toString() + " " + timeMs + " ms");
        }

    }
}
