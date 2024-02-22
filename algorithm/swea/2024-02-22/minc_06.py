import sys
sys.stdin = open('minc_06_input.txt')
sys.stdout = open('minc_06_output.txt', 'w')

for tc in range(int(input())):
    n,k = map(int,input().split())
    result = 0

    arr = [list(map(int,input().split())) for _ in range(n)]

    for i in range(n):
        cnt = 0
        for j in range(n):
            # 1 이라면 카운트
            if arr[i][j]==1:
                cnt+=1
            else:
                # 0을 만났을 때 현재까지 1의 갯수가 k와 같다면 result 1 증가
                if cnt==k:
                    result+=1
                # 0을 만났으니 cnt 0으로 초기화
                cnt=0
        # arr[i][j]가 을 만났을 때 cnt가 k인지 확인하는 과정에서 result를 증가시키게 된다.
        # 하지만 if-else문을 사용했기 때문에 마지막 숫자가 0이 아닌 1일 때 cnt가 k인 상태로 종료되면
        # 0을 만나는 분기를 실행하지 못하므로 2차 for문이 종료된 시점에 cnt가 k라면 result를 증가시켜줘야한다.
        if cnt==k:
            result+=1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1: # arr[j][i]==1 일때
                cnt += 1
            else: # arr[j][i] == 0 일 때
                if cnt==k: # 앞에서 3글자가 맞았을 경우 result 1 증가 및 cnt = 0 초기화
                    result += 1
                cnt=0
        if cnt == k:
            result += 1

    print(f'#{tc+1} {result}')



