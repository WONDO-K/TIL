import sys
input = sys.stdin.readline

t = int(input())
dp = [0]*1_000_001
dp[0],dp[1],dp[2]=1,1,2

for i in range(3,1_000_001):
    dp[i] = dp[i-1]%1_000_000_009 + dp[i-2]%1_000_000_009 + dp[i-3]%1_000_000_009

for _ in range(t):
    n = int(input())
    print(dp[n]%1_000_000_009)