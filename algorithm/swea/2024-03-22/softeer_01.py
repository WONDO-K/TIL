import sys

input = sys.stdin.readline
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(visit, depth, x, y):
    global result

    if depth == m:
        result += 1
        return

    if y == way[depth][1] and x == way[depth][0]:
        dfs(visit, depth + 1, x,y)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dfs(visit, depth, nx, ny)
                visit[nx][ny] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
way = []
result = 0

for _ in range(m):
    a,b = map(int, input().split())
    way.append((a - 1, b - 1))  # 인덱스 0번부터 시작

visited[way[0][0]][way[0][1]] = 1
dfs(visited, 1, way[0][0], way[0][1])

print(result)