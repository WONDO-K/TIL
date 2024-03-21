import sys

sys.stdin = open('1249_input.txt')

from heapq import heappop, heappush

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    pq = []
    heappush(pq, (0, 0, 0))
    distance[0][0] = 0

    while pq:
        dist, x, y = heappop(pq)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_dist = dist + arr[nx][ny]
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))


for tc in range(int(input())):
    n = int(input())
    # arr = [list(input().split()) for _ in range(n)]
    arr = []
    for _ in range(n):
        temp = list(input())
        arr.append(list(map(int, temp)))

    INF = float('inf')
    distance = [[INF] * n for _ in range(n)]
    dijkstra()
    print(f'#{tc + 1} {distance[n - 1][n - 1]}')
