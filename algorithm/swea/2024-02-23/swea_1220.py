import sys
sys.stdin = open('1220_input.txt')
sys.stdout = open('1220_output.txt', 'w')

for tc in range(10):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0

    for i in range(100):
        flag = 0
        for j in range(100):
            if arr[j][i] == 1:
                flag = 1
            if flag == 1 and arr[j][i] == 2:
                ans += 1
                flag = 0

    print(f'#{tc+1} {ans}')
