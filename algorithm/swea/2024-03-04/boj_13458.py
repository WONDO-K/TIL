import sys
input = sys.stdin.readline

n = int(input())
cls = list(map(int,input().split()))

manager1,manager2 = map(int,input().split())

cnt=0
for i in range(len(cls)):
    cls[i] -= manager1
    cnt+=1
    if cls[i] < 0: # 학생수가 음수가 되면 0으로 초기화한다. 2명 담당 가능할 때 1명도 담당이 가능하기 때문
        cls[i] = 0
# print(f'1 manager cls : {cls}')
# print(f'1 manager cnt : {cnt}')
# cls : 시험장 학생 수가 0이 되면 모든 감독관이 배치되었음을 의미
if sum(cls)==0:
    print(cnt)
else:
    while True:
        if sum(cls)==0:
            break
        else:
            while True:
                if sum(cls) == 0:
                    break
                for i in range(len(cls)):
                    if cls[i]!=0:
                        #print(f'before : {cls}')
                        cls[i]-=manager2
                        #print(f'after : {cls}')
                        cnt+=1
                        #print(f'cnt:{cnt}')
                        if cls[i]<0:
                            cls[i]=0
                        #print(f'after trans : {cls}')
                #print(f'while cls : {cls}')
    print(cnt)
