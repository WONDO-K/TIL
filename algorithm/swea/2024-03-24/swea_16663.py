import sys
sys.stdin = open('16663_input.txt')


for tc in range(int(input())):

    n, arr = input().split()
    arr = list(arr)
    result = []

    for i in range(int(n)):
            arr[i] = bin(int(arr[i],16))[2:].zfill(4)

    print(f'#{tc+1}',end=' ')
    for i in arr:
        print(i,end='')
    print()