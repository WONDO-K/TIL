package hello.hello_spring.repository;

import hello.hello_spring.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;


public interface MemberRepository {
    Member save(Member member);
    Optional<Member> findById(Long id); //Optional java8의 문법으로 findBy로 정보를 가져올 때 null일 수 있는데 Optional로 감싸서 리턴한다.(null 처리)
    Optional<Member> findByName(String name);
    List<Member> findAll();
}
