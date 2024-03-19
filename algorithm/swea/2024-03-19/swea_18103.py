import sys

sys.stdin = open('18103_input.txt')
sys.stdout = open('18103_output.txt', 'w')


def sol(now, cnt, battery):
    global min_cnt

    if cnt > min_cnt:
        return

    # 현재 위치가 n-1이면 최소 교환 횟수를 갱신
    if now == n - 1:
        min_cnt = min(min_cnt, cnt)
        return

    # 충전소를 들리지 않고 최대 이동 가능거리에 있는 정류장으로 이동하는 경우
    if now + battery < n:
        sol(now + battery, cnt + 1, stop[now + battery])

    # 충전소를 곧바로 들리는 경우
    for i in range(1, battery):
        if now + i < n:
            sol(now + i, cnt + 1, stop[now + i])


for tc in range(int(input())):
    temp = list(map(int, input().split()))

    # 정류장 수
    n = temp[0]

    # 정류장 별 배터리 용량
    stop = temp[1:] + [0]

    min_cnt = float('inf')  # 최소 교환 횟수 초기화
    
    # 제일 처음 충전소에서 충전한 횟수는 카운트 하지 않기 때문에 -1 빼주고 시작
    sol(0, -1, stop[0])

    print(f'#{tc + 1} {min_cnt}')
