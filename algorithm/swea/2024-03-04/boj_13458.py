import sys
input = sys.stdin.readline

n = int(input())
cls = list(map(int,input().split()))

manager1,manager2 = map(int,input().split())


for i in range(len(cls)):
    cls[i] -= manager1

while True:
    print(f'cls : {cls}')
    # 0보다 작거나 같아야
    if sum(cls)==0:
        break
    # 각 반에 총감독은 무조건 1명이 있어야함
    for i in range(len(cls)):
        cls[i] -= manager1
        if cls[i]<0:
            cls[i]=0
    idx=0
    cnt=3
    while True:
        print(f'idx:{idx},cnt:{cnt}')
        print(f'cls:{cls}')
        if sum(cls) == 0:
            break
        else:
            cls[idx]-=manager2
            cnt += 1
            if cls[idx] < 0:
                cls[idx] = 0
print(cnt)