import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = 10

for tc in range(1,T+1):
    N = int(input())
    building = list(map(int,input().split()))
    cnt=0

    for i in range(len(building)):
        current_build = building[i]
        if current_build == 0:
            continue

        build_m_2 = building[i - 2]
        build_m_1 = building[i - 1]
        build_p_1 = building[i + 1]
        build_p_2 = building[i + 2]

        if build_m_2<current_build and build_m_1<current_build and  build_p_1<current_build and build_p_2<current_build:

            max_v = max(build_p_2, build_p_1, build_m_2, build_m_1)
            cnt += (current_build - max_v)

    print(f'#{tc} {cnt}')
