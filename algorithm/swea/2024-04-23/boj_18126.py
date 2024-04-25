import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    que = deque()
    que.append(1)

    while que:
        now = que.popleft()
        for next,cost in arr[now]:
            # 다음 노드까지의 거리가 0이상이라면 이미 들렸다는 의미
            if dist[next] > 0:
                continue
            dist[next] += dist[now] + cost
            que.append(next)



n = int(input())
arr = [[] for _ in range(n+1)]
dist = [0] * (n+1)
sum_v = 0
for _ in range(n-1):
    start, end, cost = map(int, input().split())
    arr[start].append((end,cost))
    arr[end].append((start,cost))
bfs(1)
print(max(dist))