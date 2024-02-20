import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    result = []

    for i in range(M-1,len(arr)):
        sum_v = 0
        for j in range(0,M):
            sum_v+= arr[i-j]
        result.append(sum_v)
    print(f'#{tc} {max(result)-min(result)}')



