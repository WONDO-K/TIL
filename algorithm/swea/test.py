import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

#상하좌우

# 우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]


T = int(input())
for tc in range(T):

    N = int(input())
    print((N))
    arr = [[0 for i in range(N)] for j in range(N)]
    print(arr)
    x,y,num = 0,0,0

    while True:
        for i in range(N):
            num+=1
            x+=dx[1]
            y+=dy[1]
            arr[x][y]=num
        -=1



    