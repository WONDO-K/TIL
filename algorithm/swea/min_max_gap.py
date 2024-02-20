import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    min_index = arr.index(min(arr))
    max_v = arr[0]
    max_index = 0
    for i in range(1,len(arr)):
        if arr[i] >= max_v:
            max_v = arr[i]
            max_index = i

    print(f'#{tc} {abs(max_index-min_index)}')
