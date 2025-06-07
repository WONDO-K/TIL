# Statement와 PreparedStatement의 차이점
JDBC에서 Statement와 PreparedStatement는 모두 SQL의 실행을 담당하지만, 사용 방식과 성능, 보안 측면에서 차이가 존재한다.

## Statement 클래스
Statement 클래스는 문자열 연결을 이용해 SQL을 동적으로 구성해야 한다.
이러한 특성으로 인해 SQL 인젝션 공격에 취약하다는 단점이 있다.
```java
Statement stmt = conn.createStatement();
ResultSet rs =  30")" >stmt.executeQuery("select * from users where age > 30");
```

## PreparedStatement
반면 PreparedStatement는 동적으로 파라미터를 바인딩할 수 있는 기능을 제공한다.
값을 바인딩하면 내부적으로 Escape 처리하기 때문에 SQL 인젝션 공격을 방지할 수 있다.
```java
String sql = "SELECT * FROM users WHERE age > ? AND gender = ?";
PreparedStatement pstmt = conn.prepareStatement(sql);
pstmt.setInt(1, 30);           // 첫 번째 ? → age > 30
pstmt.setString(2, "female");  // 두 번째 ? → gender = 'female'
ResultSet rs = pstmt.executeQuery(); // (인덱스,값)의 순서로 파라미터 구성
```

또한 쿼리 ㅋ구조를 미리 확정하고 플레이스 홀더를 활용하여 값을 바인딩하는 PreparedStatement를 사용하면 SQL 구문 분석 결과를 캐싱할 수 있어 반복 실행 시 Statement보다 성능이 더 높다고 알려져 있다.

### SQL Injection 방어와 이스케이프 처리

PreparedStatement는 사용자가 입력한 값을 SQL 구문과 분리하여 전달하기 때문에 SQL 인젝션 공격을 방지할 수 있다. 내부적으로는 사용자의 입력값을 **이스케이프(Escape) 처리**하여, SQL 구문으로 인식되지 않도록 만든다.

예를 들어, Statement에서는 다음과 같은 쿼리가 만들어질 수 있다:
```java
String name = "' OR 1=1 --";
String query = "SELECT * FROM users WHERE username = '" + name + "'";
System.out.println(query);
// 출력: SELECT * FROM users WHERE username = '' OR 1=1 --'
```
이처럼 `1=1`은 항상 참이고, `--`는 SQL에서 주석을 의미하기 때문에 이후 구문이 모두 무시되어 인증 없이 우회되는 문제가 발생한다.

반면, PreparedStatement는 아래처럼 안전하게 동작한다:
```java
String sql = "SELECT * FROM users WHERE username = ?";
PreparedStatement pstmt = conn.prepareStatement(sql);
pstmt.setString(1, "' OR 1=1 --");
```
→ 이 경우 `' OR 1=1 --`은 단순 문자열로 취급되어 조건문으로 해석되지 않는다.

#### ✅ `--`가 사용되는 이유
- SQL Injection에서 `--`는 **한 줄 주석 처리**를 의미한다.
- 이를 통해 공격자는 쿼리의 뒤쪽(예: `AND password = ...`)을 무시하고, 인증 조건을 무력화할 수 있다.

| 사용 요소 | 설명 |
|-----------|------|
| `1=1`     | 항상 참이 되는 조건 |
| `--`      | 이후 SQL을 주석 처리하여 실행되지 않도록 함 |

---