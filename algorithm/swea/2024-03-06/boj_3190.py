import sys
from collections import deque
input = sys.stdin.readline

#우
dx = [0]
dy = [1]

def bfs(dir):
    cnt=0
    while dir:
        tale = deque([1,1])
        sec,way = dir.popleft()
        sec = int(sec)
        que = deque()
        que.append(([1,1]))
        # 2번 while문이 중지되었을 때 판단 기준
        flag = True
        while que:
            x,y = que.popleft()
            for i in range(sec):
                nx = x+dx[0]
                ny = y+dy[0]
                if not visit[nx][ny] and arr[nx][ny]!=3:
                    if arr[nx][ny]==2:
                        arr[nx][ny]=0
                        que.append(([nx,ny]))
                        cnt+=1
                    else:
                        tale.popleft()
                        que.append(([nx,ny]))
                        cnt += 1

                # 자신의 몸에 도달하거나 벽에 도달하면 반복문 탈출
                elif visit[nx][ny]==1 or arr[nx][ny]==3:
                    flag=False
                    break
        # 2번 while문이 중지되었다면 반복문 탈출        
        if flag == False:
            break






# 보드의 크기
n = int(input())
arr = [[0]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]
visit[1][1]=1
# 사과의 갯수
k = int(input())

# 테두리에 벽 세우기
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            arr[i][j] = 3

# 사과의 위치는 2로 표시한다.
for _ in range(k):
    i,j = map(int,input().split())
    arr[i-1][j-1] = 2


# 방향전환 횟수
l = int(input())

direction=deque()

for _ in range(l):
    direction.append(list(input().split()))
print(direction)

bfs(direction)