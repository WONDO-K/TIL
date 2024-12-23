import sys
input = sys.stdin.readline

n = int(input())
color = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n)]

for idx in range(n):
    for rgb in range(3):
        if rgb == 0:
            dp[idx][rgb] = min(dp[idx-1][1],dp[idx-1][2]) + color[idx][rgb] # dp 테이블의 0번대가 0으로 비어있기 때문에 가격정보는 color에서 가져오면 해결된다.
        if rgb == 1:
            dp[idx][rgb] = min(dp[idx-1][0],dp[idx-1][2]) + color[idx][rgb]
        if rgb == 2:
            dp[idx][rgb] = min(dp[idx-1][0],dp[idx-1][1]) + color[idx][rgb]

print(min(dp[-1]))
