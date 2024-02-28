import sys
sys.stdin = open('1861_input.txt')
sys.stdout = open('1861_output.txt','w')

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    que = deque([(x,y)])
    cnt=1

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] - arr[x][y] == 1:
                    que.append((nx,ny))
                    cnt+=1
    return cnt




for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visits = [[0 for i in range(n)] for j in range(n)]
    room = 0
    max_cnt = -float('inf')
    result = []
    for i in range(n):
        for j in range(n):
            cnt = bfs(i,j)
            if cnt == max_cnt:
                room = min(room, arr[i][j])
            elif cnt > max_cnt:
                max_cnt = cnt
                room = arr[i][j]

    print(f'#{tc+1} {room} {max_cnt}')