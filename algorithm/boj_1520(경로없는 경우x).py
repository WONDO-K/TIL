import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def recur(y,x):

    if x == m-1 and y == n-1:
        return 1

    if dp[y][x]:
        return dp[y][x]

    route = 0

    for i in range(4):
        
        ny = y+dy[i]
        nx = x+dx[i]

        if 0<=nx<m and 0<=ny<n:
            if arr[ny][nx] < arr[y][x]:
                route+=recur(ny,nx)
    dp[y][x] = route            
    return dp[y][x]

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]
recur(0,0)
print(dp[0][0])
