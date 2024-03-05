import sys,copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(point,virus):
    global max_area
    while point:
        now_arr = copy.deepcopy(arr)
        block = point.popleft()
        # 위치 순서를 좌표로 변환 후 해당 위치에 벽 세우기
        for num in block:
            now_arr[(num - 1) // m][(num - 1) % m] = 1
        cnt = 0

        que = deque()
        for j,i in virus:
            que.append(([j,i]))
        que.append(([0,0]))

        while que:
            x,y = que.popleft()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if now_arr[nx][ny]==0:
                        now_arr[nx][ny]=2
                        que.append(([nx,ny]))
        # print(f'after temp')
        # for i in now_arr:
        #     print(i)
        # print()
        cnt=0
        # 반복문 종료 시 안전 영역 수 파악
        for i in now_arr:
            cnt+= i.count(0)
        max_area = max(max_area,cnt)


n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]


temp=[]
# 0인 경우만 고려해야하기 때문에 0이 아닌 위치의 숫자를 제외한 조합을 만들기 위한 선별 작업
for j in range(m):
    for i in range(n):
        if arr[j][i]==0:
            temp.append(m*i+j+1)
point = deque(combinations(temp, 3))
print(point)
virus = deque()

for j in range(m):
    for i in range(n):
        if arr[j][i] == 2:
            virus.append([j,i])

max_area = -float('inf')
bfs(point,virus)

print(max_area)

