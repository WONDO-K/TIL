import sys
input = sys.stdin.readline

def dfs(leng,idx):
    global min_v
    if leng == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visit[i]==1 and visit[j]==1:
                    start+=arr[i][j]
                elif visit[i]==0 and visit[j]==0:
                    link+=arr[i][j]
        min_v = min(min_v,abs(start-link))
        return
    for i in range(idx,n):
        if visit[idx]==0:
            visit[idx]=1
            dfs(leng+1,i+1)
            visit[idx]=0


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = []
visit = [0]*n
min_v = float('inf')
dfs(0,0)
print(min_v)
