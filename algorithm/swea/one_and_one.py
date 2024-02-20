import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = list(map(int,input()))
    cnt = 0

    idx = 0
    for i in range(N):
        sub_cnt = 0
        if arr[i]==1:

            while i<N and arr[i]!=0:
                i+=1
                sub_cnt+=1
            cnt = max(cnt,sub_cnt)

    print(f'#{tc} {cnt}')
