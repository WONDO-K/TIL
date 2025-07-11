


# Spring Boot 슬라이스 테스트

## ✅ 슬라이스 테스트란?
- 특정 레이어만 잘라서(Controller, Service 등) 테스트하는 방식
- 불필요한 Bean은 제외하고 필요한 Bean만 로드 → 빠르고 가벼운 테스트 가능

❗ @SpringBootTest는 모든 Bean을 로드 → 느리고 무거움 → 통합 테스트에 적합

---

## ✅ 슬라이스 테스트 주요 어노테이션

| 어노테이션         | 설명                            |
|--------------|-----------------------------------|
| @WebMvcTest     | Controller 레이어 테스트           |
| @DataJpaTest    | Repository(JPA) 테스트           |
| @JsonTest       | JSON 관련 테스트                 |
| @RestClientTest | RestTemplate 등 REST 클라이언트 테스트 |

---

## ✅ @WebMvcTest 사용 예시

```java
@WebMvcTest(UserVehicleController.class)
public class UserVehicleControllerTests {

    @Autowired
    private MockMvc mvc;

    @MockBean
    private UserVehicleService userVehicleService;

    @Test
    public void testExample() throws Exception {
        given(userVehicleService.getVehicleDetails("sboot"))
            .willReturn(new VehicleDetails("Honda", "Civic"));

        mvc.perform(get("/sboot/vehicle").accept(MediaType.TEXT_PLAIN))
            .andExpect(status().isOk())
            .andExpect(content().string("Honda Civic"));
    }
}
```

- MockMvc → 요청/응답 테스트
- @MockBean → Service 등 실제 Bean 대신 Mock 객체 주입

---

## ✅ 왜 슬라이스 테스트를 사용하는가?

| 구분             | @SpringBootTest                             | 슬라이스 테스트 (@WebMvcTest 등)       |
|----------------|---------------------------------------|------------------------------------|
| 컨텍스트 로드    | 전체 애플리케이션 컨텍스트 로드 → 느림        | 필요한 레이어만 로드 → 빠름, 가벼움       |
| 사용 목적        | 통합 테스트, 전체 흐름 검증                  | 단위 테스트, 특정 레이어만 검증          |
| 테스트 속도 및 효율 | 느림, 디버깅 어려움                        | 빠름, 명확한 책임 분리 가능              |

---

## ✅ Mock 사용 시 주의사항
- 실제 환경과 다를 수 있어 신뢰도 떨어짐
- 내부 구현 변경 시 테스트 누락 가능성
- 복잡한 로직일수록 통합 테스트도 반드시 필요

✔️ Mock 적합한 상황:
- 랜덤 값/시간 사용
- 외부 시스템 호출
- 복잡한 하위 레이어 회피

---

## ✅ 결론
- 빠른 피드백 & 가벼운 테스트 → 슬라이스 테스트 사용
- Mock 남발 X → 필요할 때만 사용
- 중요한 로직 → 반드시 통합 테스트 병행
