import sys
sys.stdin = open('1865_input.txt')
sys.stdout = open('1865_output.txt', 'w')

def sol(emp,max_v):
    global max_p
    # n명 계산이 완료되었다면

    if max_v<max_p:
        return

    if emp == n:
        if max_p<max_v:
            max_p=max_v
        return

    for i in range(n):
        if not visit[i] and work[emp][i]!=0:
            max_v = max_v * (work[emp][i]/100)
            visit[i] = 1
            sol(emp+1,max_v)
            visit[i] = 0
            max_v = max_v * (100 / work[emp][i])

for tc in range(int(input())):
    n = int(input())
    work = [list(map(int,input().split())) for _ in range(n)]
    visit = [0]*n
    max_p = -float('inf')
    sol(0,1)
    print(f'#{tc+1} {(max_p*100):.6f}')
