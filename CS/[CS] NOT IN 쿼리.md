# NOT IN 쿼리를 사용할 때 발생할 수 있는 문제
```SQL
SELECT p 
FROM Post p
WHERE p.id NOT IN :postIds
```
위와 같이 NOT IN을 사용한 쿼리는 직관적이고 사용하기 쉽지만, 대규모 데이터셋에서 심각한 성능 저하를 일으킬 수 있다.

## 문제점
- NOT IN은 부정 조건으로 대부분의 DBMS에서 전체 테이블 스캔이나 인덱스 풀 스캔을 유발한다.
전체 테이블을 스캔한 후 조건에 맞지 않는 레코드를 필터링 해야하기 떄문에 데이터베이스 옵티마이저가 효율적인 실행 계획을 세우기가 어렵다.
- 인덱스를 효과적으로 활용하지 못한다.
IN 절은 인덱스 Range Scan을 통해 빨게 처리할 수 있지만, NOT IN은 인덱스 활용도가 현저히 떨어진다.
- 대량의 값을 IN 절에 넣으면 실행 계획 생성이 늘어나고, 파싱 및 최적화 단계에서 추가적인 오버헤드가 발생한다.
- NULL 값 처리 로직으로 인한 예상치 못한 결과가 발생할 수 있다. 예를 들어, column NOT IN (1,2,NULL)은 항상 빈 결과를 반환한다.

## 3값 논리(Three-valued logic)
```sql
SELECT * FROM table WHERE column NOT IN (1, 2, NULL);
```
이 쿼리의 값은 항상 0건이다.

SQL에서는 조건식이 다음 세 가지 중 하나로 평가된다.
- TRUE
- FALSE
- UNKNOWN <- NULL이 관련되면 나오는 결과
NOT IN (1, 2, NULL)은 다음과 같은 조건을 의미한다.
```sql
column ≠ 1 AND column ≠ 2 AND column ≠ NULL
# 여기서 문제가 되는 부분은 column ≠ NULL → 결과는 FALSE가 아니라 UNKNOWN
```
즉 column이 어떤 값이든 간에 NULL과의 비교 연산은 무조건 항상 UNKNOWN이 되며,
전체 조건 중 AND column =! NULL은 항상 UNKNOWN이 된다.

테이블이 아래와 같다고 가정하면
column
1
2
3
```sql
SELECT * FROM table WHERE column NOT IN (1, 2, NULL);
```
column = 1 -> FALSE
column = 2 -> FALSE
column = 3 ->
    -> 3!=1 -> TRUE
    -> 3!=2 -> TRUE
    -> 3!=NULL -> UNKNOWN
TRUE AND TRUE AND UNKNOWN -> 전체결과 UNKNOWN
SQL은 WHERE 절에서 UNKNOWN을 FALSE로 간주하기 때문에
→ column = 3도 반환되지 않음


## 최적화 방안
- NOT EXISTS 활용
```sql
SELECT p FROM Post p
WHERE NOT EXISTS (
    SELECT 1 FROM Post temp
    WHERE temp.id = p.id AND temp.id IN :postIds
)
```
NOT EXISTS는 행 단위로 평가되어 매칭되는 첫 행을 찾자마자 평가를 중단한다.
이는 DBMS가 '존재하지 않음'을 확인하기 위해 특별히 최적화된 방식
대규모 데이터셋에서 가장 안정적이고 확장성 있는 성능을 제공

- LEFT JOIN + IS NULL 패턴
```sql
SELECT p FROM Post p 
LEFT JOIN (
    SELECT temp.id FROM Post temp WHERE temp.id IN :postIds
) filtered ON p.id = filtered.id
WHERE filtered.id IS NULL
```
이 방식은 서브쿼리 결과가 작을 때 특히 효율적. 인덱스를 효과적으로 활용할 수 있으며, PK 인덱스를 사용한 JOIN 연산이 최적화된다.