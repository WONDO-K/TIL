package hello.core.scan.filter;

import java.lang.annotation.*;

@Target(ElementType.TYPE) // 제일 중요함 타입이 어디에 붙는지(필드? 클래스? 등)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MyIncludeComponent {
}
