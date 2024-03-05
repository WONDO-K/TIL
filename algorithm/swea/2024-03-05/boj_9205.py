import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    que = deque()
    que.append(home)

    while que:
        x,y = que.popleft()

        if abs(x-fest[0])+abs(y-fest[1])<=1000:
            print('happy')
            return
        else:
            for i in range(n):
                if not visit[i]:
                    nx,ny = conv[i]
                    if abs(x-nx)+abs(y-ny)<=1000:
                        visit[i]=1
                        que.append(([nx,ny]))
    print('sad')
    return
# tc
for tc in range(int(input())):
    # 편의점 갯수
    n = int(input())
    home = list(map(int,input().split()))
    conv = [list(map(int,input().split())) for _ in range(n)]
    fest = list(map(int,input().split()))

    visit = [0]*(n)
    bfs()