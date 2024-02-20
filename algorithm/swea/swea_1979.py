import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')



T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = []
    cnt=0
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    # 행 선회
    for i in range(N):
        letter = 0
        for j in range(N):
            if arr[i][j] == 1:
                letter += 1
                if arr[i][j+1]<N and letter==K:
                    cnt+=1
            else:




    print(f'col = {cnt}')

    print(f'#{tc} {cnt}')
