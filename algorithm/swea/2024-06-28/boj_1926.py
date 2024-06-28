import sys
input = sys.stdin.readline
from collections import deque

row, col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(row)]
visit = [[0]*col for _ in range(row)]

max_area = 0
pic_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c):
    global max_area
    cnt = 1
    q = deque()
    q.append((r, c))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<row and 0<=ny<col and board[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1


    max_area = max(max_area, cnt)


for i in range(row):
    for j in range(col):
        if board[i][j] == 1 and not visit[i][j]: # 현재 위치가 1이거나 방문하지 않았다면
            visit[i][j] = 1 # bfs가 동작하기 전에 방문처리를 해준다.
            bfs(i, j)
            pic_cnt += 1

print(pic_cnt, max_area, sep='\n')