import sys
input = sys.stdin.readline

def dfs(arr):
    if len(arr) == m:
        print(' '.join(map(str,arr)))

    for i in range(n):
        if not visit[i]:
            visit[i]=1
            arr.append(nums[i])
            dfs(arr)
            arr.pop()
            visit[i]=0


n,m = map(int,input().split())

nums = [i for i in range(1,n+1)]

visit = [0] * n
result = []
dfs(result)