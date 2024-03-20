import sys
sys.stdin = open('1238_input.txt')
sys.stdout = open('1238_output.txt', 'w')

from collections import deque

def bfs(start):
    visit[start]=1

    que = deque()
    que.append(start)

    while que:
        now = que.popleft()

        for next in arr[now]:
            if not visit[next]:
                que.append(next)
                visit[next]= visit[now]+1



for tc in range(10):
    n,m = map(int,input().split())

    arr = [[] for _ in range(101)]
    visit = [0] * (101)

    pair = list(map(int,input().split()))
    for i in range(0,len(pair),2):
        a,b = pair[i],pair[i+1]
        arr[a].append(b)

    bfs(m)
    max_v = -1
    ans_idx = 0
    for idx,value in enumerate(visit):
        if value >= max_v:
            max_v = value
            ans_idx = idx
    print(f'#{tc+1} {ans_idx}')