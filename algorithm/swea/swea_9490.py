import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

def solve(x,y,move):
    sum = 0
    for move_cnt in range(1,move+1):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = x + (dx[i] * move_cnt)
            ny = y + (dy[i] * move_cnt)
            if 0 <= nx <N and 0 <= ny < M:
                sum+=arr[nx][ny]
    return sum

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    arr = []

    for _ in range(N):
        arr.append(list(map(int,input().split())))

    result_max = 0
    for i in range(N):
        for j in range(M):
            max_v = solve(i,j,arr[i][j])
            max_v+=arr[i][j]
            result_max = max(result_max, max_v)

    print(f'#{tc} {result_max}')





