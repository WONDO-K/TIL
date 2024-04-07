import sys
input=sys.stdin.readline

n = int(input())
liq = list(map(int,input().split()))
liq.sort()

v = float('inf')
x,y = 0,0
start,end = 0,n-1

while start < end: # start와 end가 만나면 같은 인덱스의 값들을 sum_v로 만듦

    sum_v = liq[start]+liq[end]

    if abs(sum_v) <= v: # 절대값이 0에 가까워지려면 기준값보다 계속 같거나 작아져야함
        x = liq[start]
        y = liq[end]
        v = abs(sum_v)

    if sum_v <= 0: # 1번 if와 별개로 진행되어야함 elif x
        start += 1
    else: # sum_v > 0:
        end -= 1

print(x,y)



