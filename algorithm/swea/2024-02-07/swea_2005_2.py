import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    N = int(input())

    arr = [0] * N
    arr[0] = [1]

    for i in range(1,N):
        temp = [1]*(i+1)
        print(temp)
        for j in range(1,i):
            temp[j] = arr[i-1][j-1] + arr[i-1][j]
        arr[i] = temp

    print(f'#{tc + 1}')
    for i in arr:
        print(*i)

