import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(y,x):
    dist = 0
    visit[y][x]=1
    que = deque()
    que.append([y,x]) 

    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<m and 0<=nx<n:
                if arr[ny][nx] == 'L' and visit[ny][nx]==0:
                    visit[ny][nx] = visit[y][x]+1 # dist 배열을 따로 만들지 않고 visit를 그대로 활용
                    que.append([ny,nx])
                    dist = visit[y][x]+1
    return dist-1 # 시작점 제외 (다음칸으로 한칸 이동시 소요시간이 1시간 즉, 시작점은 카운트하지 않는다.)

m,n = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(m)]


max_dist = 0

for j in range(m):
    for i in range(n):
        if arr[j][i]=='L':
            visit = [[0 for _ in range(n)] for _ in range(m)] # 매 노드마다 거리 측정을 위한 새로운 visit이 필요하다.
            max_dist = max(max_dist,bfs(j,i))

print(max_dist)