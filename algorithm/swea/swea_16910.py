import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())
for tc in range(T):
    N = int(input())
    cnt=0
    for i in range(N+1):
        for j in range(N+1):
            if (i**2) + (j**2) <= (N**2):
                cnt+=1
    # 좌표평면은 총 4 사분면으로 구성되어 있으며 위의 반복문은 1개의 사분면의 갯수를 카운팅한다.
    # 그래서 이 cnt 값을 4개 곱하여 주면 4개의 사분면의 원소 갯수를 알 수 있지만 0,0 원점의 갯수가 3번 더 카운팅 되며
    # 또한 x축,y축이 각 두번씩 중복되어 총 8번 카운팅된다
    # 이를 cnt*4의 값에서 x,y축 4번 초과 카운팅된 부분을 빼주고 0,0 3번 카운팅을 빼준다.

    cnt = (cnt*4) - (N*8)//2 -3
    print(f'#{tc+1} {cnt}')