import sys
input = sys.stdin.readline

n,q = map(int, input().split())
visit = [0]*(n+1)

for i in range(q):
    land = int(input())
    point = land

    flag = 0

    while True:
        print(f'point : {point}')
        if point == 1:
            break

        if visit[point]:
            print(f'visit[{point}] : {visit[point]}')
            print(point)
            flag = 1
            break
        else:
            point //= 2

    if flag == 0:
        print(0)
        visit[land] =1


