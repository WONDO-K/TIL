import sys
from collections import deque
sys.stdin = open('18621_input.txt')
sys.stdout = open('18621_output.txt', 'w')

def bfs(start):
    global cnt

    if visit[start]:
        return

    que = deque()
    que.append(start)
    visit[start]=1
    cnt += 1

    while que:
        now = que.popleft()
        for next in arr[now]:
            if not visit[next]:
                visit[next]=1
                que.append(next)
            else:
                cnt-=1

for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    visit = [0] * (n + 1)
    pair = list(map(int,input().split()))

    # Union 연산을 각각 수행
    for i in range(0,len(pair),2):
        a,b = pair[i],pair[i+1]
        arr[a].append(b)

    cnt=0
    for i in range(1,n+1):
        bfs(i)
    print(f'#{tc+1} {cnt}')