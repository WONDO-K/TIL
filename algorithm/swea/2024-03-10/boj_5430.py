from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    
    # 수행 동작
    p = input().strip()
    
    # 배열의 길이
    n=int(input())

    # 에러 확인을 위한 플래그
    error=0
    
    # 대괄호와 , 를 제외한 숫자들만 사용
    num=input().strip()
    que = deque(num[1:-1].split(','))
    
    # 배열의 길이가 0도 포함이기 때문에 0일때 빈 덱으로 초기화
    if n==0:
        que = deque()
        
    revers_cnt = 0
    for command in p:
        if command == 'R':
            revers_cnt+=1
        elif command == 'D':
            if len(que)==0:
                error=1
                break
            else:
                if revers_cnt%2==0:
                    que.popleft()
                else:
                    que.pop()

    if error==0:
        if revers_cnt%2==0: # cnt가 짝 수이면 역순 2회 즉 역순을 하지 않은 상태임
            print("["+",".join(que)+"]")
        else: # cnt가 홀 수이면 역순을 1번한 것과 같은 상태
            que.reverse()
            print("[" + ",".join(que) + "]")
    else:
        print('error')


        