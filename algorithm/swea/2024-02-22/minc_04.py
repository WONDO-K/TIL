import sys
sys.stdin = open('minc_04_input.txt')
sys.stdout = open('minc_04_output.txt', 'w')

for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n+1)]
    result = [[0 for i in range(m)] for i in range(n+1)]

    ans = arr[0]
    max_v = float("-inf")
    min_v = float("inf")

    for i in range(1,n+1):
        for j in range(m):
            if arr[0][j] == arr[i][j]:
                result[i][j] = result[i][j-1]+1
        max_v = max(max_v,sum(result[i]))
        min_v = min(min_v,sum(result[i]))
    print(f'#{tc+1} {max_v-min_v}')