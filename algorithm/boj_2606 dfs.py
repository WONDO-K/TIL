import sys

input = sys.stdin.readline

def dfs(x):
    global cnt
    visit[x]=1
    cnt+=1

    for nx in arr[x]:
        if visit[nx] != 1:
            dfs(nx)

    

n = int(input())
m = int(input())
visit = [0 for _ in range(n+1)]
arr = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
dfs(1)
print(cnt-1)