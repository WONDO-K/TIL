import sys
input = sys.stdin.readline

row, col = map(int, input().split())

board = [list(input().strip()) for _ in range(row)]
visit = [[0]*col for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global s, w
    stack = [(x, y)]
    while stack: # 스택을 사용하면 재귀함수를 사용하지 않아도 된다.
        x, y = stack.pop() # 스택의 후입선툴로 빼주면 현재 분기가 모두 종료되었을 때 이전 분기로 돌아갈 수 있기 때문에 dfs의 특징을 유지한다.
        if board[x][y] == 'v': # 늑대면
            w += 1
        elif board[x][y] == 'o': # 양이면
            s += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] != '#' and not visit[nx][ny]:
                visit[nx][ny] = 1
                stack.append((nx, ny))

sheep, wolf = 0, 0

for i in range(row):
    for j in range(col):
        s, w = 0, 0 # 양, 늑대의 수를 초기화
        if board[i][j] != '#' and not visit[i][j]: # 현재 위치가 #이 아니거나 방문하지 않았다면
            visit[i][j] = 1 # dfs가 동작하기 전에 방문처리를 해준다.
            dfs(i, j)

            if s > w: # dfs가 끝나고 양이 더 많다면
                sheep += s
            else: # 늑대가 더 많거나 같다면
                wolf += w
    
print(sheep, wolf)
