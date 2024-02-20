import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def solve(x, y):
    sum_v=0
    for i in range(M):
        for j in range(M):
            sum_v+=arr[x+i][y+j]
    return sum_v

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    sum_v = 0
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v=max(sum_v,solve(i,j))
    print(f'#{tc} {sum_v}')


