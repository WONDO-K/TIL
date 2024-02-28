import sys
sys.stdin = open('1861_input.txt')
sys.stdout = open('1861_output.txt','w')

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    cnt=1
    start_x = x
    start_y = y
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] - arr[x][y] == 1:
                x,y = nx,ny
                cnt+=1
    return cnt


for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visits = [[0 for i in range(n)] for j in range(n)]
    room = 0
    max_cnt = -float('inf')
    result = []
    for i in range(n):
        for j in range(n):
            cnt = dfs(i,j)

            if cnt>max_cnt:
                max_cnt=cnt
                if room == 0:
                    room = arr[i][j]
                elif room > arr[i][j]:
                    room = arr[i][j]

    print(f'#{tc+1} {room} {max_cnt}')