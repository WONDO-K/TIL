import sys
sys.stdin = open('16971_input.txt')
sys.stdout = open('16971_output.txt', 'w')

from heapq import heappop,heappush


def dijkstra(start):
    pq = []

    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)

        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_node = to[0]
            next_dist = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist  # 누적 거리를 최단 거리로 갱신
            heappush(pq, (new_dist, next_node))

for tc in range(int(input())):

    n,e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    INF = float('inf')
    distance = [INF] * (n+1)
    for _ in range(e):
        start,end,point = map(int,input().split())
        graph[start].append([end,point])

    dijkstra(0)
    print(f'#{tc+1} {distance[n]}')