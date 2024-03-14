from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

que = deque()

for i in range(1,n+1):
    que.append(i)

print("<" , end='')

while que:
    for i in range(k-1): # 만약 3번이라면 2번만 이동하면 bottom에 k번째 수가 위치함
        que.append(que.popleft())
    print(que.popleft(),end='')
    if que: # que에 원소가 남아 있으면 ,를 출력한다. 없으면 마지막 원소를 출력했기 때문에 ,가 필요없음
        print(', ',end='')

print(">")