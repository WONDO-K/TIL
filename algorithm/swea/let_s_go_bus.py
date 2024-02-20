import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    bus = []
    station = [0 for _ in range(5001)]

    for _ in range(N):
        bus.append(list(map(int,input().split())))
    P = int(input())

    idx = []
    for _ in range(P):
        idx.append(int(input()))

    for start, end in bus:
        for i in range(start,end+1):
            station[i]+=1

    result = []
    for i in idx:
        result.append(station[i])

    print(f'#{tc} ',end='')
    print(*result)