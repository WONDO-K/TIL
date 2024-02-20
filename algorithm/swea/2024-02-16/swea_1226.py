import sys
sys.stdin = open('1226_input.txt')
sys.stdout = open('1226_output.txt','w')

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    visit[x][y] = 1
    que.append((x,y))

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<16 and 0<=ny<16:
                if arr[nx][ny]!=1 and visit[nx][ny]!=1:
                    visit[nx][ny]=1
                    que.append((nx,ny))



for tc in range(10):
    n = int(input())
    #arr = [list(map(int,input())) for i in range(16)]
    visit = [[0 for _ in range(16)] for _ in range(16)]
    arr = []

    start = [0,0]
    goal = [0,0]

    for i in range(16):
        temp = list(map(int,input()))
        if 2 in temp:
            start[0] = i
            start[1] = temp.index(2)
        if 3 in temp:
            goal[0] = i
            goal[1] = temp.index(3)
        arr.append(temp)


    bfs(start[0],start[1])
    print(f'#{tc+1} {visit[goal[0]][goal[1]]}')
