import sys
from collections import deque
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,way):

    que = deque()
    que.append(([i,j]))

    way_idx=3
    sec = 0
    flag = True
    while que:
        x,y = que.popleft()
        move_cnt, direction = way.popleft()
        move_cnt = int(move_cnt)

        if flag == False:
            break
        nx,ny=0,0
        for i in range(1,move_cnt+1):
            nx = x + dx[way_idx]*i
            ny = y + dy[way_idx]*i
            sec += 1  # 시간 증가
            if 1<=nx<n+1 and 1<=ny<n+1:
                # 다음 좌표가 사과라면
                if arr[nx][ny] == 2:
                    arr[nx][ny]=1 # 다음 좌표를 1로 변경
                # 다음 좌표가 빈칸이라면
                elif arr[nx][ny]==0: 
                    arr[nx][ny]=1 # 다음칸에 머리
                    arr[x][y]=0 # 이전칸 꼬리를 줄이기
                elif arr[nx//i][ny//i]==1: # 다음 좌표가 뱀의 몸에 닿는다면 종료
                    flag=False
                    break
            else:
                flag=False
                break
        if flag==True:
            # break 없이 for문이 종료되면 que에 다음 좌표 삽입
            que.append(([nx,ny]))

        if way_idx == 0:
            if direction == 'D':
                way_idx=3
            else:
                way_idx=2
        elif way_idx == 1:
            if direction == 'D':
                way_idx=2
            else:
                way_idx=3
        elif way_idx == 2:
            if direction == 'D':
                way_idx=0
            else:
                way_idx=1
        else:
            if direction == 'D':
                way_idx=1
            else:
                way_idx=0

    return sec



n = int(input())

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]


apple_cnt = int(input())

for _ in range(apple_cnt):
    x,y = map(int,input().split())
    arr[x][y]=2

way_cnt = int(input())

way = deque()
for _ in range(way_cnt):
    way.append(list(input().split()))

ans = bfs(1,1,way)

for i in arr:
    print(i)

print(ans)