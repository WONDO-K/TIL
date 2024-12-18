import sys

input = sys.stdin.readline

def recur(idx,weight):

    if weight > k: # 초과 조건이 종료 조건보다 먼저 검증되어야함
        return -9999999
    
    # 종료 조건이 먼저 검증되면 무게가 초과하더라도 종료 조건인 idx==n이 되면 초과조건 검증하지 않고 0을 리턴하기 때문
    if idx == n: 
        return 0
    
    
    if dp[idx][weight] != -1: # 이미 저장된 값이라면 연산 x
        return dp[idx][weight]
    
    dp[idx][weight] = max(
        recur(idx+1,weight),
        recur(idx+1,weight+w[idx])+v[idx]
        )
    return dp[idx][weight]
    

n,k = map(int,input().split())

w = [i for i in range(n)]
v = [i for i in range(n)]

for i in range(n):
    wi,vi = map(int,input().split())
    w[i],v[i] = wi, vi

dp = [[-1 for _ in range(k+1)] for _ in range(n)]

print(recur(0,0))