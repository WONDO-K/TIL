import sys
from heapq import heappop,heappush
sys.stdin = open('prim_input.txt')


def dijkstra(start):
    pq = []
    
    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        
        # 최단 거리 노드에 대한 정보
        dist,now = heappop(pq)

    
        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]
            
            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist # 누적 거리를 최단 거리로 갱신
            heappush(pq,(next_dist,next_node)) # next_node의 인접 노드를 pq에 추가


v, e = map(int, input().split())  # n: 정점의 수, e: 간선의 수
graph = [[] for _ in range(v)]
INF = float('inf')
distance = [INF] * v

# 간선 정보 저장
for _ in range(e):
    s,e,p = map(int, input().split())  # a <-> b, c: 거리
    graph[s].append([p,e])

dijkstra(0)
print(distance)

