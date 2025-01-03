import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def recur(y,x):

    if x == m-1 and y == n-1:
        return 1

    if dp[y][x]!=-1: # -1과 0은 계산이 아직 안이루어진 값, 계산 후에도 이동 가능 경로가 없는 경우로 구분해야함
        return dp[y][x]

    dp[y][x] = 0 # 여기서 0으로 일단 초기화를 해준다는 것은 재귀함수에 진입한 값은 일단 이동이 가능한 구역이라는 의미

    for i in range(4):
        
        ny = y+dy[i]
        nx = x+dx[i]

        if 0<=nx<m and 0<=ny<n:
            if arr[ny][nx] < arr[y][x]:
                dp[y][x]+=recur(ny,nx)         
    return dp[y][x]

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]

print(recur(0,0))
