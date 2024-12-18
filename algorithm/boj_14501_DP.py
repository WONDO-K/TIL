import sys

input = sys.stdin.readline

def recur(idx):
    if idx == n+1:
        return 0

    if idx > n+1:
        return -9999999999
    
    if dp[idx] != -1: # 이미 저장되었다면
        return dp[idx]

    # 상담을 받거나, 안받거나, 그 중에서 더 많은 돈을 버는 경우를 DP에 저장하겠다.
    dp[idx] = max(recur(idx + t[idx]) + p[idx],recur(idx+1))

    return dp[idx]

n = int(input())

t = [ i for i in range(n+1)]
p = [ i for i in range(n+1)]

dp = [ -1 for _ in range(n+1) ]

for i in range(1,n+1):
    ti, pi = map(int,input().split())
    t[i],p[i] = ti, pi

print(recur(1))