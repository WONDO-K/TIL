package hello.core.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class MemberServiceImpl implements MemberService{

    private final MemberRepository memberRepository; // 추상화에만 의존 AppConfig에서 생성자 주입
    
    // 생성자를 통해 어떤 객체를 주입할지 정해야함
    @Autowired // MemberRepository타입에 맞는 클래스를 찾아와서 자동으로 연결해서 주입해준다.
    // ac.getBean(MemberRepository.class) 처럼 동작한다. (다른 동작들이 더 있긴 하지만)
    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public void join(Member member) {
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId) {
        return memberRepository.findById(memberId);
    }

    // 테스트 용
    public MemberRepository getMemberRepository(){
        return memberRepository;
    }
}
