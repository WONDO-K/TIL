import sys
input = sys.stdin.readline

n = int(input())
color = [list(map(int,input().split())) for _ in range(n)]

# dp 테이블을 따로 만들어서 하려니 dp[0] 번대의 값들이 모두 0으로 되어있어서 0번대 인덱스의 색깔들을 계산하지 못함
# color 테이블을 그대로 사용
for idx in range(1,n):
    color[idx][0] = min(color[idx-1][1],color[idx-1][2]) + color[idx][0]
    color[idx][1] = min(color[idx-1][0],color[idx-1][2]) + color[idx][1]
    color[idx][2] = min(color[idx-1][0],color[idx-1][1]) + color[idx][2]

print(min(color[-1]))
