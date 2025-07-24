# Private 메서드에 @Transactional 선언하면 트랜잭션이 동작하는가?
기본적으로 @Transactional, @Cahced, @Async 등의 어노테이션은 런타미에 동작하는 Spring AOP를 사용하여 동작한다.
Spring AOP가 제공하는 JDK Dynamic Proxy, CGLIB Proxy 방식 모두 타깃이 구현하는 인터페이스나 구체 클래스를 대상으로 프록시를 만들어서 타깃 클래스의 메서드 수행 전후에 횡단 관심사에 대한 처리를 할 수 있다.

Spring은 빈 생성시, 해당 빈에 AOP 어노테이션이 있는지 검사하고, 있다면 프록시 객체를 생성하여 빈을 대체한다(빈을 주입한다).
AOP 적용 대상인 클래스의 경우, 즉, @Transactional과 같은 AOP 어노테이션이 하나라도 선언된 클래스의 경우, 해당클래스는 프록시로 감싸진다.

JDK Dynamic Proxy의 경우 타겟 클래스가 구현하는 인터페이스를 기준으로 프록시를 생성하여 public 메서드만 AOP에 적용 가능하다.
CGLIB Proxy의 경우 인터페이스를 구현하지 않는 클래스를 상속하여 프록시를 생성하기 때문에 private를 제외한 public, protected, package-private 메서드에 AOP를 적용할 수 있다.

```java
@Slf4j  
@RequiredArgsConstructor  
@Service  
public class SelfInvocation {  
  
    private final MemberRepository memberRepository;  
  
    public void outerSaveWithPublic(Member member) {  
        /**
         * 같은 클래스 내부 호출이기 때문에, 프록시를 거치지 않고 자기 자신(This)의 메서드를 직접 호출
         * -> 이 경우에 AOP가 개입하지 못하기 떄문에 트랜잭션이 적용되지 않음
         * -> AOP는 외부에서 프록시 객체를 통해 메서드가 호출될 때만 적용되기 때문이다.
        */
        saveWithPublic(member); 
    }  
  
    @Transactional  
    public void saveWithPublic(Member member) {  
        log.info("call saveWithPublic");  
        memberRepository.save(member);  
        throw new RuntimeException("rollback test");  
    }  
  
    public void outerSaveWithPrivate(Member member) {  
        saveWithPrivate(member);  
    }  
  
    @Transactional  
    private void saveWithPrivate(Member member) {  
        log.info("call saveWithPrivate");  
        memberRepository.save(member);  
        throw new RuntimeException("rollback test");  
    }  
}

public interface MemberRepository extends JpaRepository<Member, Long> {  
}
```
```java
@SpringBootTest  
class SelfInvocationTest {  
  
    private static final Logger log = LoggerFactory.getLogger(SelfInvocationTest.class);  
  
    @Autowired  
    private SelfInvocation selfInvocation;  
  
    @Autowired  
    private MemberRepository memberRepository;  
  
    @AfterEach  
    void tearDown() {  
        memberRepository.deleteAllInBatch();  
    }  
  
    @Test  
    void aopProxyTest() {  
        // @Transactional 애너테이션을 가지고 있으므로, 빈이 Proxy 객체로 대체되어 주입된다.  
        assertThat(AopUtils.isAopProxy(selfInvocation)).isTrue();  
        // interface를 구현하지 않은 클래스이므로 CGLIB Proxy가 생성된다.  
        assertThat(AopUtils.isCglibProxy(selfInvocation)).isTrue();  
    }  
  
    @Test  
    void outerSaveWithPublic() {  
        Member member = new Member("test");  
  
        try {  
            selfInvocation.outerSaveWithPublic(member);  
        } catch (RuntimeException e) {  
            log.info("catch exception");  
        }  
  
        List<Member> members = memberRepository.findAll();  
        // self invocation 문제로 인해 트랜잭션이 정상 동작하지 않음.  
        // 예외 발생으로 인한 롤백이 동작하지 않고 남아있음.
    
      assertThat(members).hasSize(1);  
    }  
  
    @Test  
    void outerSaveWithPrivate() {  
        try {  
            selfInvocation.outerSaveWithPrivate(new Member("test"));  
        } catch (RuntimeException e) {  
            log.info("catch exception");  
        }  
  
        List<Member> members = memberRepository.findAll();  
  
        // self invocation 문제로 인해 트랜잭션이 정상 동작하지 않음.  
        // 예외 발생으로 인한 롤백이 동작하지 않고 남아있음.        assertThat(members).hasSize(1);  
    }  
  
    @Test  
    void saveWithPublic() {  
        Member member = new Member("test");  
  
        try {  
            selfInvocation.saveWithPublic(member);  
        } catch (RuntimeException e) {  
            log.info("catch exception");  
        }  
  
        List<Member> members = memberRepository.findAll();  
  
        // 외부에서 프록시 객체를 통해 메서드가 호출되었기 때문에 트랜잭션 정상 동작, 롤백 성공.  
        assertThat(members).hasSize(0);  
    }  
}
Spring AOP는 외부에서 프록시 객체를 통해 메서드가 호출될 때만 AOP 어드바이스(트랜잭션 관리)를 적용한다. 같은 클래스 내에서 메서드를 호출하면, 프록시를 거치지 않고 직접 호출되므로 트랜잭션 어드바이스가 적용되지 않는다.

이를 해결하기 위해서는 자기 자신을 프록시로 주입 받아 프록시를 통해 메서드를 호출하거나, 별도의 클래스로 분리하거나, AspectJ를 이용하는 방법이 있다. AspectJ를 사용하면 동일 클래스 내에서의 메서드 호출에도 AOP 어드바이스를 적용할 수 있다.

자기 자신을 프록시로 주입 받는 방법
@Slf4j  
@RequiredArgsConstructor  
@Service  
public class SelfInvocation {  
  
    private final MemberRepository memberRepository;  

    /**
     * SelfInvocation 빈을 생성하려면 SelfInvocation이 필요하다는 것을 의미한다.
     * 그런데 생성자 주입에 SelfInvocation이 필요하다고 선언되어 있음.
     * 즉 자기 자신을 생성하기 위해 자기 자신이 필요한 상황이 발생함
     * 여기서 순환 의존성이 발생하게 된다. -> BeanCurrentlyInCreationException
    */
    private final SelfInvocation selfInvocation;  // 자기 자신을 프록시로 주입 받는다.  
  
    public void outerSaveWithPublic(Member member) {
        /**
         * 자기 자신을 프록시로 주입받고 selfInvocation. 메서드 호출을 통해 외부에서 프록시를 거쳐 메서드를 호출하는 효과를 얻는다.
         * */  
        selfInvocation.saveWithPublic(member);  
    }  
  
    @Transactional  
    public void saveWithPublic(Member member) {  
        log.info("call saveWithPublic");  
        memberRepository.save(member);  
        throw new RuntimeException("rollback test");  
    }
    ...
}
```
위의 방법은 순환 의존성 문제를 일으킬 수 있으므로, 권장되지 않는 방법이다.

## 별도의 클래스로 분리하는 방법
```java
@Slf4j  
@RequiredArgsConstructor  
@Service  
public class TransactionService {  
  
    @Transactional  
    public void outer() {  
        log.info("call outer");  
        logCurrentTransactionName();  
        logActualTransactionActive();  
        inner();  
    }  
  
    @Transactional(propagation = Propagation.REQUIRES_NEW)  
    public void inner() {  
        log.info("call inner");  
        logCurrentTransactionName();  
        logActualTransactionActive();  
    }  
  
    private void logActualTransactionActive() {  
        boolean actualTransactionActive = TransactionSynchronizationManager.isActualTransactionActive();  
        log.info("actualTransactionActive = {}", actualTransactionActive);  
    }  
  
    private void logCurrentTransactionName() {  
        String currentTransactionName = TransactionSynchronizationManager.getCurrentTransactionName();  
        log.info("currentTransactionName = {}", currentTransactionName);  
    }  
}

// 로그
// call outer  
// currentTransactionName = server.transaction.TransactionService.outer  
// actualTransactionActive = true  
// call inner  
// currentTransactionName = server.transaction.TransactionService.outer  
// actualTransactionActive = true
outer가 inner 메서드를 호출하는데, outer의 propagation 속성은 REQUIRED, inner는 REQUIRES_NEW로 서로 다른 트랜잭션으로 분리되어야 합니다. 하지만, 로그를 보면 동일한 outer의 트랜잭션에 속해있다. 이처럼 트랜잭션 전파 속성이 다른 두 메서드가 동일한 클래스 내부에서 self invocation 호출하면 의도대로 동작하지 않는다. 이 때 outer와 inner 메서드를 각각 다른 클래스로 분리하여 호출하면 해결할 수 있다.

// OuterTransactionService
@Slf4j  
@RequiredArgsConstructor  
@Service  
public class OuterTransactionService {  
  
    private final InnerTransactionService innerTransactionService;  
  
    @Transactional  
    public void outer() {  
        log.info("call outer");  
        logCurrentTransactionName();  
        logActualTransactionActive();  
        innerTransactionService.inner();  
    }  
  
    private void logActualTransactionActive() {  
        boolean actualTransactionActive = TransactionSynchronizationManager.isActualTransactionActive();  
        log.info("actualTransactionActive = {}", actualTransactionActive);  
    }  
  
    private void logCurrentTransactionName() {  
        String currentTransactionName = TransactionSynchronizationManager.getCurrentTransactionName();  
        log.info("currentTransactionName = {}", currentTransactionName);  
    }  
}

// InnerTransactionService
@Slf4j  
@RequiredArgsConstructor  
@Service  
public class InnerTransactionService {  
  
    @Transactional(propagation = Propagation.REQUIRES_NEW)  
    public void inner() {  
        log.info("call inner");  
        logCurrentTransactionName();  
        logActualTransactionActive();  
    }  
  
    private void logActualTransactionActive() {  
        boolean actualTransactionActive = TransactionSynchronizationManager.isActualTransactionActive();  
        log.info("actualTransactionActive = {}", actualTransactionActive);  
    }  
  
    private void logCurrentTransactionName() {  
        String currentTransactionName = TransactionSynchronizationManager.getCurrentTransactionName();  
        log.info("currentTransactionName = {}", currentTransactionName);  
    }  
}

// 로그
// call outer  
// currentTransactionName = server.transaction.OuterTransactionService.outer  
// actualTransactionActive = true  
// call inner  
// currentTransactionName = server.transaction.InnerTransactionService.inner  
// actualTransactionActive = true
```
이렇게 각각 프록시를 생성할 수 있는 클래스로 분리하면 AOP 어드바이스가 정상적으로 적용되어, outer와 inner 메서드가 서로 다른(독립적인) 트랜잭션으로 동작하게 된다.

---

## 💡 면접에서는 이런 식의 질문으로도 나올 수 있어요

### Q1. `@Transactional`이 적용되지 않는 경우는 언제인가요?
A1. 내부 메서드 호출(Self Invocation), private 메서드, final 클래스 또는 final 메서드 등은 Spring AOP 기반의 `@Transactional`이 적용되지 않습니다. 이는 프록시 기반의 AOP가 동작하기 위한 조건이 충족되지 않기 때문입니다.

### Q2. `@Transactional(propagation = REQUIRES_NEW)`으로 설정했는데, 기존 트랜잭션과 분리되지 않았습니다. 왜 그런가요?
A2. 같은 클래스 내에서 메서드가 호출되는 Self Invocation 상황이라면, 프록시를 거치지 않으므로 트랜잭션 전파 옵션이 적용되지 않습니다. 이를 해결하려면 메서드를 별도의 클래스로 분리하거나, 프록시 객체를 통해 호출되도록 구조를 변경해야 합니다.

### Q3. `@Transactional`이 붙은 메서드에서 예외가 발생했지만 롤백이 되지 않았습니다. 원인이 뭘까요?
A3. 기본적으로 `@Transactional`은 `RuntimeException` 또는 `Error`에 대해서만 롤백합니다. 체크 예외는 별도로 `rollbackFor` 속성에 명시해줘야 롤백됩니다. 또한, 예외가 프록시 바깥으로 전파되어야 트랜잭션 매니저가 이를 감지하고 롤백을 수행합니다.

### Q4. 자기 자신을 주입받아서 프록시로 사용하면 안 되나요?
A4. 생성자 주입을 사용할 경우 순환 의존성 문제가 발생하므로 권장되지 않습니다. Setter나 `@PostConstruct`를 활용하거나, 가장 좋은 방법은 해당 메서드를 별도의 클래스로 분리하여 사용하는 것입니다.

### Q5. REQUIRES_NEW와 REQUIRED의 차이점은 무엇인가요?
A5. REQUIRED는 기존 트랜잭션이 있으면 참여하고, 없으면 새로 시작합니다.
반면 REQUIRES_NEW는 항상 새로운 트랜잭션을 시작하며, 기존 트랜잭션은 일시 중단됩니다. 트랜잭션 간 영향을 차단하고 싶을 때 사용합니다.