import sys
sys.stdin = open('16656_input.txt')
sys.stdout = open('16656_output.txt','w')

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while que:
        x,y = que.popleft()
        if arr[x][y] == 3:
            return visit[x][y] - 2
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]!=1 and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y]+1
                    que.append((nx,ny))
    return 0



for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    que = deque()


    goal = [0,0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                visit[i][j]+=1
                que.append((i,j))
                ans = bfs()
    # if ans == None:
    #     ans=0
    print(f'#{tc+1} {ans}')