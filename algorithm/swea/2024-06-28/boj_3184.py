import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

row, col = map(int, input().split())

board = [list(input().strip()) for _ in range(row)]
visit = [[0]*col for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global s, w
    if board[x][y] == 'v': # 늑대면
        w += 1
        
    elif board[x][y] == 'o': # 양이면
        s += 1


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<row and 0<=ny<col and board[nx][ny] != '#' and not visit[nx][ny]:
            visit[nx][ny] = 1
            dfs(nx, ny)

sheep, wolf = 0, 0

for i in range(row):
    for j in range(col):
        s, w = 0, 0 # 양, 늑대의 수를 초기화
        if board[i][j] != '#' and not visit[i][j]: # 현재 위치가 #이 아니거나 방문하지 않았다면
            visit[i][j] = 1 # bfs가 동작하기 전에 방문처리를 해준다.
            dfs(i, j)

            if s > w: # dfs가 끝나고 양이 더 많다면
                sheep += s
            else: # 늑대가 더 많거나 같다면
                wolf += w
    
print(sheep, wolf)