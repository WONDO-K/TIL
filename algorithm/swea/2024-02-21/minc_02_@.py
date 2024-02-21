import sys
sys.stdin = open('minc_02_input.txt')
sys.stdout = open('minc_02_output.txt', 'w')

def solve(start_i,start_j):
    target = arr[start_i][start_j]
    global result
    for i in range(N):
        for j in range(N):
            cnt=0
            if target == arr[i][j]:
                for k in range(start_i,i+1):
                    for z in range(start_j,j+1):
                        cnt+=1
            result.append(cnt)
            print(f'result : {result}')
    print(result)
    return max(result)

T = int(input())

for tc in range(T):
    N = int(input())

    arr=[]
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    result=[]
    max_area = 0
    for i in range(N):
        for j in range(N):
            max_area = max(max_area,solve(i,j))
            mac_cnt = result.count(max_area)
    print(f'#{tc+1} {mac_cnt}')