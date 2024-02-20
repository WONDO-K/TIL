import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(1,11):
    dump = int(input())
    arr = list(map(int,input().split()))

    while 0<dump:
        max_v = arr[arr.index(max(arr))]
        min_v = arr[arr.index(min(arr))]
        if (max_v-min_v) == 1 or (max_v-min_v) == 0:
            break
        else:
            arr[arr.index(max(arr))]-=1
            arr[arr.index(min(arr))]+=1
            dump-=1

    print(f'#{tc} {arr[arr.index(max(arr))]-arr[arr.index(min(arr))]}')



