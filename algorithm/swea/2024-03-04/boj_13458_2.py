import sys
input = sys.stdin.readline

n = int(input())
cls = list(map(int,input().split()))

manager1,manager2 = map(int,input().split())

cnt=0
# 총감독관은 1명만 배치 가능하기 때문에 뺄셈으로 계산한다.
for i in range(n):
    cls[i] -= manager1
    cnt += 1

    if cls[i]>0:
        if cls[i]%manager2==0:
            cnt += cls[i]//manager2
        else:
            # 배수가 아니면 나머지가 발생한다. 나머지를 커버하기 위해 1명의 부감독관을 더 배치한다.
            cnt += cls[i]//manager2+1
print(cnt)

