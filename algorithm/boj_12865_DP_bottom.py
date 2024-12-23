import sys

input = sys.stdin.readline

n,k = map(int,input().split())

w = [i for i in range(n+1)]
v = [i for i in range(n+1)]

for i in range(1,n+1): # dp 배열의 idx가 1부터 시작되어야 하기 때문에 w,v도 1부터 시작하게끔
    wi,vi = map(int,input().split())
    w[i],v[i] = wi, vi

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]


for idx in range(1,n+1): # dp 배열이 1부터 사용되어야 함
    for weight in range(1,k+1):
        if weight < w[idx]: # 현재 무게한계 보다 지금 넣을 물건의 무게거 더 무거우면 넣지 못한다.
            # 물건을 넣지 않는 경우
            dp[idx][weight] = dp[idx-1][weight] # 이전까지의 최대 가치를 그대로 가져온다.
        else: # 역순이 아닌 정방향이기 때문에 idx를 더하는 것이 아니라 뺀다.
            # 물건을 넣는 경우
            # weight - w[idx]는 물건을 넣고 남은 공간에 해당함
            # 즉 1~k 까지의 무게 한계의 최대 가치를 모두 저장하는 구조이기 때문
            dp[idx][weight] = max(dp[idx-1][weight], dp[idx-1][weight-w[idx]]+v[idx])

print(dp[n][k])


# import sys

# input = sys.stdin.readline

# n,k = map(int,input().split())
# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]


# for idx in range(1,n+1):
#     weight,value = map(int,input().split())
#     for w in range(1,k+1):
#         if w < weight:
#             dp[idx][w] = dp[idx-1][w]
#         else: # 역순이 아닌 정방향이기 때문에 idx를 더하는 것이 아니라 뺀다.
#             dp[idx][w] = max(dp[idx-1][w], dp[idx-1][w-weight]+value)

# print(dp[n][k])