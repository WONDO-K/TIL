import sys
sys.stdin = open('01_input.txt')
sys.stdout = open('01_output.txt', 'w')

# 이동시 우회전 방향
di = [1,2,3,0]
    # 북 동 남 서 : 각 방향을 바라보고 있을 시에 우회전 방향 벡터
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solve(direction,):

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    print(arr)