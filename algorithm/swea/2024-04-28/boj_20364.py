import sys
input = sys.stdin.readline

n,q = map(int, input().split())
visit = [0]*(n+1)

for i in range(q):
    land = int(input())
    point = land

    first = 0

    while True:
        print(f'point : {point}')
        if point == 1:
            break

        if visit[point]:
            print(f'visit[{point}] : {visit[point]}')
            first = point

        point//=2
        print(f'after point : {point}')
    if first:
        print(first)
    else: # 방문 x
        print(0)
        visit[land] = 1


