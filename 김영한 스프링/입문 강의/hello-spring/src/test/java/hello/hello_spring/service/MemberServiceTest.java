package hello.hello_spring.service;

import hello.hello_spring.domain.Member;
import hello.hello_spring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest { // test는 과감하게 한글로 네이밍해도 실제 코드에 포함되지 않기 때문에 무관하다.

    MemberService memberService;
    MemoryMemberRepository memberRepository;

    @BeforeEach
    public void beforeEach() { // 각 테스트 시작전 memberRepository를 만들어 MemberService에 넣어준다. -> 동일한 MemoryMemberRepository를 사용할 수 있다.
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);
    }

    @AfterEach
    public void afterEach(){
        memberRepository.clearStore();
    }


    @Test
    void 회원가입() {
        // given (기반 데이터)
        Member member = new Member();
        member.setName("spring");

        // when (이것을 검증)
        Long saveId = memberService.join(member);

        // then (검증부)
        Member findMember= memberService.findOne(saveId).get();
        assertThat(member.getName()).isEqualTo(findMember.getName()); // alt+enter로 줄일 수 있다.
    }

    @Test
    public void 중복_회원_예외(){
        // given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when
        memberService.join(member1);
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));

        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");

//        try{
//            memberService.join(member2);
//            fail();
//        } catch (IllegalStateException e){
//            assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
//        }

        // then

    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}