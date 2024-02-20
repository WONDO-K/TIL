import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

#https://campkim.tistory.com/12

def dfs(start):
    stack = [start]

    while stack:
        x = stack.pop()
        for nx in arr[x]:
            if not visited[nx]:
                stack.append(nx)
                visited[nx]=1



for tc in range(10):
    T,L = map(int,input().split())
    temp = list(map(int,input().split()))

    arr = [[] for _ in range(100)]

    for i in range(0,len(temp),2):
        arr[temp[i]].append(temp[i+1])
    visited = [0 for _ in range(100)]
    dfs(0)
    print(f'#{tc+1} {visited[99]}')


