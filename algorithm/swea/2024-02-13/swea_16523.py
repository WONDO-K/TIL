import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')
#from functools import lru_cache


    # 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#@lru_cache(maxsize=128, typed=False)
def dfs(x,y):
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # nx,ny가 배열 범위를 벗어나지 않으며 아직 방문하지 않았고 arr[nx][ny]가 0(통로)일 떄
        if 0<=nx<N and 0<=ny<N and visit[nx][ny]!=1 and arr[nx][ny]!='1':
            # arr[nx][ny]!='1'를 통해 0과 3의 경우의 수만 분기를 통과할 수 있기 때문에 검증 필요x
            dfs(nx,ny)

for tc in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]
    visit = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = [i,j]
            elif arr[i][j] == '3':
                end = [i, j]

    visit[start[0]][start[1]] = 1
    dfs(start[0],start[1])
    print(f'#{tc+1} {visit[end[0]][end[1]]}')



