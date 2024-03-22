import sys
sys.stdin = open('7465_input.txt')

from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    visit[start] = 1
    while que:
        now = que.popleft()
        for next in way[now]:
            if not visit[next]: # 다음 좌표를 방문하지 않았다면
                visit[next]=1
                que.append(next)

for tc in range(int(input())):
    n,m = map(int,input().split())

    way = [[] for _ in range(n+1)]
    visit = [0]*(n+1)
    cnt=0

    for _ in range(m):
        a,b = map(int,input().split())
        way[a].append(b)
        way[b].append(a)

    for i in range(1,n+1):
        if not visit[i]:
            bfs(i)
            cnt += 1
    print(f'#{tc+1} {cnt}')