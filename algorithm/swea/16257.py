import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(1,int(input())+1):

    arr = [[0 for _ in range(10)]for _ in range(10)]

    N = int(input())
    cnt = 0
    for _ in range(N):
        paint = list(map(int,input().split()))
        color = paint.pop()


        for i in range(paint[0],paint[2]+1):
            for j in range(paint[1],paint[3]+1):
                if arr[i][j] != color:
                    arr[i][j] += color
                    if arr[i][j] == 3:
                        cnt+=1


    print(f'#{tc} {cnt}')
