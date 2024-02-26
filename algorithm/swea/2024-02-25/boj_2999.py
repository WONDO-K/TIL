import sys
from collections import deque
input = sys.stdin.readline

arr = deque(input().rstrip())
n=len(arr)
temp=[]
r,c=0,0
for i in range(1,n//2+1): # 1부터 n의 절반값 까지만 계산해야 중복된 r,c 조합이 생기지 않는다.
    for j in range(i,n+1):
        if i*j == n:
            r,c = i,j # 계속해서 갱신하다 보면 가장 i가 큰 값으로 r이 갱신된다.

result = [[0 for i in range(c)] for j in range(r)]

for i in range(c):
    for j in range(r): # 1. 같은 열 기준으로 행을 먼저 탐색한다.
        result[j][i] = arr.popleft()

for i in result:
    print(''.join(i),end='')