import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')


T = int(input())

for tc in range(1,T+1):

    K,N,M = map(int,input().split())
    charge = list(map(int,input().split()))

    cnt=0
    start=0

    while start+K<N:
        for move in range(K,0,-1):
            if start+move in charge:
                start+=move
                cnt+=1
                break
        else:
            cnt=0
            break

    print(f'#{tc} {cnt}')



