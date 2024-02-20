import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')


for _ in range(10):
    tc=int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int,input().split())))

    y = 99
    x = arr[99].index(2)
    while True:
        if y == 0:
            break
        # 왼쪽으로
        if x>0 and arr[y][x-1]:
            while x>0 and arr[y][x-1]:
                x-=1
            else: # 끝까지 갔을 때 위로 올라감
                y-=1
        elif x<99 and arr[y][x+1]:
            while x<99 and arr[y][x+1]:
                x+=1
            else:
                y-=1
        else:
            y-=1
    print(f'#{tc} {x}')