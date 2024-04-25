import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    que = deque()
    que.append(1)

    while que:
<<<<<<< HEAD
        now = que.popleft()
        for next,cost in arr[now]:
            # 다음 노드까지의 거리가 0이상이라면 이미 들렸다는 의미
            if dist[next] > 0:
                continue
            dist[next] += dist[now] + cost
            que.append(next)
=======
        now, cost = que.popleft()

        if visit[now][1] > cost:
            continue

        visit[now][1] = cost  # 현재 노드까지의 거리를 저장



        for next_node, next_cost in arr[now]:
            if visit[next_node][0] == 0:  # 다음 노드를 방문하지 않았을 때
                visit[next_node][0] = 1  # 다음 노드를 방문했음을 표시
                visit[next_node][1] = max(visit[next_node][1], cost + next_cost)  # 이전 노드까지의 거리에 현재 노드와의 거리를 더한 것과 이전까지 저장되어 있던 거리를 비교
                que.append((next_node, cost + next_cost))  # 다음 노드와 거리를 큐에 추가
>>>>>>> 32ff6a9a03c106c6a8d38f4336fe77db99df10e1



n = int(input())
arr = [[] for _ in range(n+1)]
dist = [0] * (n+1)
sum_v = 0
for _ in range(n-1):
    start, end, cost = map(int, input().split())
    arr[start].append((end,cost))
    arr[end].append((start,cost))
bfs(1)
<<<<<<< HEAD
print(max(dist))
=======
print(visit[n][1])
>>>>>>> 32ff6a9a03c106c6a8d38f4336fe77db99df10e1
