# 논리 삭제와 물리 삭제
논리 삭제(Soft Delete), 물리 삭제(Hard Delete)
- 물리 삭제는 DELETE 명령어를 통해 직접 데이터를 삭제하는 방식.
- 논리 삭제는 UPDATE 명령어를 통해 삭제 여부를 나타내는 컬럼을 수정하는 방식.
- 즉 물리 삭제는 실제로 데이터를 삭제하는 반면 논리 삭제는 데이터가 삭제되었음을 표시만 한다는 차이가 있음

```sql
# 물리 삭제 처리
delete from member where id = 1;

# 논리 삭제 처리와 조회
update member set deleted_at = curdate() where id = 1;
select * from member where deleted_at is null;
```

## 어떤 방식이 좋은가?
방식마다 장/단점을 고려해 상황에 맞는 선택을 해야한다.
- 물리 삭제의 경우
    - 실제로 데이터를 삭제하기 때문에 저장 공간을 새로 확보할 수 있으며, 테이블 크기를 줄여 검색 속도 향상을 기대할 수 있다.
    - 하지만 데이터 복구가 어렵다는 점과 삭제된 데이터가 비즈니스 의사결정에 사용되기 어렵다는 단점이 있다.
- 논리 삭제의 경우
    - 데이터를 삭제하지 않기 떄문에 데이터 복구에 용이하고, 비즈니스 의사결정에 사용될 수 있다.
    - 하지만, 테이블에 데이터가 많아져 성능에 악영향을 줄 수 있고, 논리적으로 삭제된 데이터를 제외하지 않고 조회하는 실수가 발생할 수 도 있다.

## JPA에서 Soft Delete 구현
- 엔티티 삭제는 실제 DELETE 쿼리가 아니라 deleted를 true로 만드는 방식임.(deleted_at에 날짜가 추가되어 있다면 논리 삭제 상태로 간주하는 방법도 있음)
    - @SqlDelete 어노테이션으로 구현
    - 모든 쿼리에 where deleted = false 구문이 필수적으로 포함되어야만 삭제되지 않은 데이터에 대해 안전한 조회가 가능하다.
    - @Where 어노테이션

```java
@NoArgsConstructor(access = PROTECTED)
@Getter
@SQLDelete(sql = "UPDATE cafe_policy SET deleted = true WHERE id = ?")
@Entity
public class CafePolicy extends BaseDate {

    @Id
    @GeneratedValue(strategy = IDENTITY)
    private Long id;

    private Integer maxStampCount;

    private String reward;

    private Integer expirePeriod;

    private Boolean deleted = Boolean.FALSE; // 기본값을 FALSE로 설정
    
    // ...
}
```

@SQLDelete(sql = "UPDATE cafe_policy SET deleted = true WHERE id = ?")
해당 문장이 .delete()가 호출될 경우, DELETE 쿼리 대신 해당 코드를 통해 UPDATE가 실행된다.

SQL Delete도 마찬가지로 곧바로 쿼리가 날아가는 것이 아니라, 영속성 컨텍스트에서 변경사항이 관리되다가 트랜잭션이 끝날 때 처리된다. 

## @Where 어노테이션
```java
@NoArgsConstructor(access = PROTECTED)
@Getter
@SQLDelete(sql = "UPDATE cafe_policy SET deleted = true WHERE id = ?")
@Where(clause = "deleted = false")
@Entity
public class CafePolicy extends BaseDate {

    @Id
    @GeneratedValue(strategy = IDENTITY)
    private Long id;

    private Integer maxStampCount;

    private String reward;

    private Integer expirePeriod;

    private Boolean deleted = Boolean.FALSE; // 기본값을 FALSE로 설정
    
    // ...
}
```
@Where(clause = "deleted = false")
이 어노테이션을 사용하면 모든 요청에 대하여 default로 where deleted=false 를 추가하여 준다.