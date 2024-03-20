import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    que.append((i,j))
    while que:
        x,y = que.popleft()
        visit[x][y]=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny]!=0 and not visit[nx][ny]:
                    que.append((nx,ny))
                    visit[nx][ny]=1
                elif arr[nx][ny]==0:
                    # 해당 위치에 접해져 있는 바닷물의 갯수를 파악하고 나중에 뺀다.
                    cnt[x][y]+=1

    return 0

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
flag = 0
year = 0
que = deque()

while True:
    cnt = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0 and not visit[i][j] :
                result.append(bfs(i,j))
    # 빙산 높이 낮추기
    for i in range(n):
        for j in range(m):
            arr[i][j]-=cnt[i][j]
            # 빙산은 0보다 낮아질 수 없다.
            if arr[i][j]<0:
                arr[i][j]=0

    if len(result)==0:
        break
    elif len(result)>=2:
        flag = 1
        break
    year+=1

if flag:
    print(year)
else:
    print(0)