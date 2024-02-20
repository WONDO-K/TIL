import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

def dfs(start):
    stack = [start]
    while stack:
        x = stack.pop()
        for nx in arr[x]:
            if not visited[nx]:
                stack.append(nx)
                visited[nx] = 1


for tc in range(int(input())):
    V,E = map(int,input().split())

    arr = [[] for _ in range(V+1)]

    for _ in range(E):
        x,nx = map(int,input().split())
        arr[x].append(nx)

    S,G = map(int,input().split())
    visited = [0 for i in range(50)]
    dfs(S)
    print(f'#{tc+1} {visited[G]}')

