import sys
from collections import deque
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make_dir(way_idx,direction):
    if way_idx == 0:
        if direction == 'D':
            way_idx = 3
        else:
            way_idx = 2
    elif way_idx == 1:
        if direction == 'D':
            way_idx = 2
        else:
            way_idx = 3
    elif way_idx == 2:
        if direction == 'D':
            way_idx = 0
        else:
            way_idx = 1
    else:
        if direction == 'D':
            way_idx = 1
        else:
            way_idx = 0
    return way_idx
def bfs(x,y,way):

    tail = deque()
    tail.append((x,y))

    way_idx=3
    sec = 0

    # 현재 몇번째 이동 명령인지 확인하기 위한 변수
    way_num = 0
    while True:
        nx = x + dx[way_idx]
        ny = y + dy[way_idx]

        if 1<=nx<n+1 and 1<=ny<n+1 and arr[nx][ny]!=1:
            # 다음 좌표가 사과라면
            if arr[nx][ny] == 2:
                arr[nx][ny]=1 # 다음 좌표를 1로 변경
                tail.append((nx, ny))
            # 다음 좌표가 빈칸이라면
            elif arr[nx][ny]==0:
                arr[nx][ny]=1 # 다음칸에 머리
                tail.append((nx, ny))
                tail_x,tail_y = tail.popleft()
                arr[tail_x][tail_y]=0
            x,y = nx,ny
            sec += 1  # 시간 증가
        else: # 벽이거나 몸에 부딪힌 경우
            sec+=1
            break
        if way_num<way_cnt and way[way_num][0] == sec :
            way_idx = make_dir(way_idx, way[way_num][1])
            way_num+=1
    return sec



n = int(input())

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]


apple_cnt = int(input())

for _ in range(apple_cnt):
    x,y = map(int,input().split())
    arr[x][y]=2

way_cnt = int(input())

way = []
for _ in range(way_cnt):
    x, c = input().split()  # 방향변환 정보
    way.append((int(x), c))  # 정보를 list에 저장

ans = bfs(1,1,way)

print(ans)