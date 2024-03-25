import bisect
import sys
sys.stdin = open('02_input.txt')

for tc in range(int(input())):
    n,q = map(int,input().split())

    mileage = list(map(int,input().split()))
    mileage.sort()
    set_m = set(mileage)
    for _ in range(q):
        m = int(input())
        # 리스트의 길이가 길어질 수록 탐색하는 시간이 너무 길어진다.
        # n의 길이만큼 살펴볼 q의 획수가 많아지기 때문에 n*q => 10억을 훌쩍 넘는다.
        if m not in set_m:
            print(f'm:{m}')
            print(f'set_m:{ set_m}')
            print(f'#{tc+1} 0')
        else:
            idx = bisect.bisect_left(mileage,m)# 삽입된 왼쪽자리
            print(f'idx : {idx}')
            # 인덱스보다 작은 수의 갯수는 인덱스의 갯수만큼 있음,
            print(f'#{tc+1} {idx*(n-idx-1)}')