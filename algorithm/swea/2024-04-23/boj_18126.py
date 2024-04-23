import sys
from collections import deque

input = sys.stdin.readline

# def bfs(start):
#     global sum_v
#
#     que = deque()
#     for i in arr[start]:
#         que.append((i[0],i[1]))
#
#     visit[start][0] = 1
#     print(que)
#     while que:
#         now,cost = que.popleft()
#         visit[now][1] = cost
#         for next_node, next_cost in arr[now]:
#
#             if visit[next_node][0] == 0:  # 다음 노드를 방문하지 않았을 때
#
#                 visit[next_node][0] = 1  # 다음 노드를 방문했음을 표시
#                 visit[next_node][1] = max(visit[next_node][1],visit[now][1] + next_cost)
#                 que.append((next_node, next_cost))  # 다음 노드와 거리를 큐에 추가
#             print(f'visit : {visit}')

def bfs(start):
    que = deque()
    for i in arr[start]:
        que.append((i[0],i[1]))

    visit[start][0] = 1  # 시작 노드를 방문했음을 표시
    while que:
        now, cost = que.popleft()
        visit[now][1] = cost  # 현재 노드까지의 거리를 저장
        for next_node, next_cost in arr[now]:
            if visit[next_node][0] == 0:  # 다음 노드를 방문하지 않았을 때
                visit[next_node][0] = 1  # 다음 노드를 방문했음을 표시
                visit[next_node][1] = max(visit[next_node][1], cost + next_cost)  # 이전 노드까지의 거리에 현재 노드와의 거리를 더한 것과 이전까지 저장되어 있던 거리를 비교
                que.append((next_node, cost + next_cost))  # 다음 노드와 거리를 큐에 추가



n = int(input())
arr = [[] for _ in range(n+1)]
visit = [ [0,0] for _ in range(n+1)]
sum_v = 0
for _ in range(n-1):
    start, end, cost = map(int, input().split())
    arr[start].append((end,cost))
    arr[end].append((start,cost))
bfs(1)
print(visit)
print(visit[n][1])