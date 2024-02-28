import sys

input = sys.stdin.readline


def get_cnt(tar):
    cnt=0
    for i in range(n):
        if tar & 0x1: # 1 비트가 1인지 확인
            cnt+=1
        # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
        tar >>= 1
    return cnt

arr=['a', 'b', 'c', 'd', 'e']

n = len(arr)

result = 0
for tar in range(1<<n):
    if get_cnt(tar)>=2:
        result+=1
print(result)