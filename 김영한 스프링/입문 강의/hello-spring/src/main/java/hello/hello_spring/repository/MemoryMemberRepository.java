package hello.hello_spring.repository;

import hello.hello_spring.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.*;

//@Repository // Repository또한 스프링에 등록해야함
public class MemoryMemberRepository implements MemberRepository{

    private static Map<Long, Member> store = new HashMap<>();
    private static long sequence = 0L;



    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(),member);

        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny(); // 하나라도 찾는지 여부
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values()); // store의 멤버들이 반환된다.
    }

    public void clearStore(){
        store.clear();
    }
}
