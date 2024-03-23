import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    que = deque()
    que.append((1,1))
    cnt = 1
    while que:

        x,y = que.popleft()
        visit[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1<=nx<m+1 and 1<=ny<m+1:
                print(f'nx : {nx}, ny : {ny}')
                if cnt == 1:
                    if arr[nx][ny]=='1' and not visit[nx][ny]:
                        visit[nx][ny] = visit[x][y]+1
                        que.append((nx,ny))
                        cnt-=1
                else:
                    if arr[nx][ny]=='0' and not visit[nx][ny]:
                        visit[nx][ny] = visit[x][y]+1
                        que.append((nx,ny))

                    else:
                        print(f'nx:{nx}, ny{ny}, stop')
                        print(f'cnt:{cnt}, arr[{nx}][{ny}] = {arr[nx][ny]}')


n,m = map(int,input().split())

arr = [['0']+list(input().rstrip()) for _ in range(n)]
visit = [[0] * (m+1) for _ in range(n+1)]
bfs()
print(visit)