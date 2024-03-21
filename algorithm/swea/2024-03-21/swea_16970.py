import sys
sys.stdin = open('16970_input.txt')

from heapq import heappop,heappush
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dijkstra():
    pq = []

    heappush(pq,(0,0,0))
    distance[0][0] = 0

    while pq:
        dist, x, y = heappop(pq)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                #if distance[nx][ny]==INF:
                # 새로운 위치까지의 연료 소비량 계산
                fuel_cost = max(0, arr[nx][ny] - arr[x][y])  # 높이 차이에 따른 연료 소비량
                new_dist = dist + 1 + fuel_cost  # 이동 비용 계산

                # 새로운 위치까지의 비용이 더 작다면 갱신하고 큐에 추가
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))
                else:
                    continue
            else:
                continue

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    INF = float('inf')
    distance = [[INF]*n for _ in range(n)]

    dijkstra()
    # for i in distance:
    #     print(i)
    print(f'#{tc+1} {distance[n-1][n-1]}')