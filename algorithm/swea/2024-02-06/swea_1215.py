import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(10):
    N = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(map(str, input())))
    cnt = 0

    for i in range(8):
        for j in range(0,8 - N + 1):
            temp = arr[i][j:j+N]
            if temp == temp[::-1]:
                cnt+=1

    for i in range(len(arr)):
        for j in range(0, 8 - N + 1):
            temp = []
            for k in range(N):
                temp.append(arr[j + k][i])
            if temp == list(reversed(temp)):
                cnt += 1
    print(f'#{tc+1} {cnt}')