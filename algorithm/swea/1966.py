import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(1,int(input())+1):

    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f'#{tc}',end=' ')

    for i in arr:
        print(i,end=' ')
    print()