import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

y,x = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(y)]


max_dist = 0

for j in range(y):
    for i in range(x):
        if arr[j][i]=='L':
            visit = [[0 for _ in range(x)] for _ in range(y)] # 매 노드마다 거리 측정을 위한 새로운 visit이 필요하다.
            dist = [[0 for _ in range(x)] for _ in range(y)]

            que = deque()
            que.append([j,i]) 
            visit[j][i]=1

            while que:
                ey, ex = que.popleft()

                for i in range(4):
                    ny = ey + dy[i]
                    nx = ex + dx[i]

                    if 0<=ny<y and 0<=nx<x:
                        if arr[ny][nx] == 'L' and visit[ny][nx] == 0:
                            visit[ny][nx] = 1
                            dist[ny][nx] = dist[ey][ex]+1 # 현재 있는 위치에서 거리를 1 더한게 다음 위치의 거리값
                            max_dist = max(max_dist,dist[ny][nx])
                            que.append([ny,nx])


print(max_dist)