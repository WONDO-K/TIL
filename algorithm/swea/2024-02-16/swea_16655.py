import sys
sys.stdin = open('16655_input.txt')
sys.stdout = open('16655_output.txt','w')

from collections import deque

def bfs():
    visit[start] += 1
    while que:
        x = que.popleft()
        for nx in arr[x]:
            if visit[nx]==0:
                visit[nx] = visit[x]+1

for tc in range(int(input())):
    v,e = map(int,input().split())
    arr = [[] for _ in range(51)]
    visit = [0 for _ in range(51)]
    que = deque()

    for _ in range(e):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    print(arr)
    start,goal = map(int,input().split())
    print(f'start:{start}, goal:{goal}')

    que.append(start)


    bfs()
    print(visit)
    print()
