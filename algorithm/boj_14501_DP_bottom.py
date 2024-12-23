import sys

input = sys.stdin.readline

n = int(input())

t = [ i for i in range(n+1)]
p = [ i for i in range(n+1)]

for i in range(1,n+1):
    ti, pi = map(int,input().split())
    t[i],p[i] = ti, pi

dp = [ 0 for _ in range(n+1) ]

for idx in range(n)[::-1]: # [::-1] 역순을 의미
    if idx + t[idx] > n :
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx + t[idx]] + p[idx],dp[idx+1])

print(dp[0]) 
