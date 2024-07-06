package hello.core.web;


import hello.core.common.MyLogger;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequiredArgsConstructor // 생성자 Autowired 자동주입
public class LogDemoController {
    private final LogDemoService logDemoService;
    private final MyLogger myLogger; // 프록시 모드로 MyLogger가 아닌 가짜 껍데기가 이 자리를 차지하고 있음

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request) throws InterruptedException {
        String requestURL = request.getRequestURL().toString();

        System.out.println("myLogger = " + myLogger.getClass());
        myLogger.setRequestURL(requestURL); //myLogger의 기능을 실제 동작할 때 진짜 myLogger가 들어온다

        myLogger.log("controller test");
        Thread.sleep(1000);
        logDemoService.login("testId");

        return "ok";

    }
}
