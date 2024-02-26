import sys
sys.stdin = open('algo1_sample_in.txt')
sys.stdout= open('algo1_sample_out.txt','w')
def solve(x,y):
    # 현재 기준점에 위치한 과녁 점수를 초기에 sum_v에 더해주고 시작한다.
    sum_v = arr[x][y]
    # 상하좌우 각 방향으로 두 칸 씩 이동할 수 있음
    move = 2

    # 1칸, 2칸 이동시 방향 벡터를 갱신해주어야 하기 때문에 함수 밖에 선언하는 평소와 달리 함수 내에서 벡터를 선언한다.
    for move_cnt in range(1,move+1):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x+dx[i]*move_cnt #방향 벡터에 현재 move_cnt를 곱해주면 각 방향으로 1칸, 2칸씩 점진적으로 탐색 가능
            ny = y+dy[i]*move_cnt
            if 0<=nx<n and 0<=ny<n: # n*n 배열을 벗어나지 않는 경우만 합산
                sum_v+=arr[nx][ny]
    return sum_v

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_v = -float('inf') # 최대값을 구해야하며 초기 최댓값은 어떠한 결과보다 작아야 갱신되기 때문에 음의 무한대로 설정한다.

    for i in range(n):
        for j in range(n):
            sum_v = solve(i,j)
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc+1} {max_v}')
