import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    global cnt
    que = deque()
    que.append(x)

    visit[x] = 1

    while que:
        x = que.popleft()
        for nx in arr[x]: # 양방향이기 떄문에 [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]] 한 노드에 여러개가 연결되어 있다.
            if visit[nx] != 1:
                que.append(nx)
                visit[nx] = 1
                cnt+=1

n = int(input())
m = int(input())

que = deque()

visit = [0 for _ in range(n+1)]
arr = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
bfs(1)
print(cnt)