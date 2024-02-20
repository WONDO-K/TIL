import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    x, y = 0, 0
    num = 0

    while True:
        # 우
        while True:
            if y >= N or arr[x][y] != 0:
                break
            if arr[x][y] == 0:
                num += 1
                arr[x][y] = num
                y += 1
        y-=1
        x+=1

        if num >= (N**2):
            break
            # 하
        while True:
            if x >= N or arr[x][y] != 0:
                break
            if arr[x][y] == 0:
                num += 1
                arr[x][y] = num
                x += 1
        x-=1
        y-=1
        if num >= (N**2):
            break
            # 좌
        while True:
            if y < 0 or arr[x][y] != 0:
                break
            if arr[x][y] == 0:
                num += 1
                arr[x][y] = num
                y-=1

        y+=1
        x-=1
        if num >= (N**2):
            break

        while True:
            if x<0 or arr[x][y] != 0:
                break
            if arr[x][y] == 0:
                num += 1
                arr[x][y] = num
                x -= 1
        x+=1
        y+=1
        if num >= (N**2):
            break
    print(f'#{tc}')

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=' ')
        print()
