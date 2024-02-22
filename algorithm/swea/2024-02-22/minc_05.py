import sys
sys.stdin = open('minc_05_input.txt')
sys.stdout = open('minc_05_output.txt', 'w')

for tc in range(int(input())):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n+1)]

    x,y=0,0
    # 2의 위치 탐색
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] == 2:
                x, y = i, j
                break

    max_v=0
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] == 1:
                # 반올림 힘수 : round, 올림 : math.ceil, 내림 : math.floor
                #dist = ((i-idx[0]) + (j-idx[1])**2)
                dist = ((abs(i - x)**2 + abs(j - y)**2))**(0.5)
                #dist = math.ceil(dist)
                max_v = max(max_v,dist)
    if max_v % 1 == 0:  # 만약 max_v가 정수라면
        print(f'#{tc + 1} {int(max_v)}')  # 정수로 출력
    else:  # 정수가 아니라면
        print(f'#{tc + 1} {int(max_v) + 1}')  # 올림 처리된 값으로 출력

