# 완전탐색 - 정수론 - 누적합 (기억)

- 1 + 2 + 3
    - 1 + 2 = 3
    - 3 + 3 = 6
    - 사람은 1+2 가 3이란 것을 알기 때문에 3+3은 6이란 것을 알지만 컴퓨터는 모른다.
- 컴퓨터 연산
    - 1 + 2 = 3 -> 이것을 기억해야함
    - 1 + 2 + 3 = 6
    - 위와 같이 동일한 과정을 한 번 더 수행함 -> 낭비 

## 재귀 함수 경우의 수 - 14501문제
```Java
import sys

input = sys.stdin.readline

def recur(idx, money):
    global max_v

    if idx >= n+1:
        max_v = max(max_v,money)
        return

    if idx+t[idx] <= n+1:
        # 상담 하는 경우
        recur(idx+t[idx], money+p[idx])
    # 상담 안하는 경우
    recur(idx+1,money)

n = int(input())

t = [ i for i in range(n+1)]
p = [ i for i in range(n+1)]

for i in range(1,n+1):
    ti, pi = map(int,input().split())
    t[i],p[i] = ti, pi

max_v = float('-inf')

recur(1,0)

print(max_v)
```
- 위의 코드는 상담을 받는, 받지 않는 모든 경우의 수를 다 검토한다.


| 일자 | 1일  | 2일  | 3일  | 4일  | 5일  | 6일  | 7일  |
|------|------|------|------|------|------|------|------|
| Ti   | 3    | 5    | 1    | 1    | 2    | 4    | 2    |
| Pi   | 10   | 20   | 10   | 20   | 15   | 40   | 200  |
- 7일차 퇴사인데 해당 날의 소요 시간이 1이라고 가정하면 무조건 받는 것이 무조건 이득이다.
- 6일차가 소요시간이 2일이라면 150만원을 벌 수 있기 때문에 상담 하는 것이 이득
- 5일차는 상담을 안받는것이 이득이다 6일차에 150만원을 벌 수 있기 때문