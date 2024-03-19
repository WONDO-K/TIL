import sys
sys.stdin = open('16938_input.txt')
sys.stdout = open('16938_output.txt', 'w')

def sol(cnt,cost):
    global min_v

    if cost>=min_v:
        return

    if cnt == n:
        if min_v > cost:
           min_v = cost
        return

    for i in range(n):
        if not visit[i]:
            cost += product[cnt][i]
            visit[i]=1
            sol(cnt+1,cost)
            visit[i]=0
            cost -= product[cnt][i]

for tc in range(int(input())):
    n = int(input())
    product = [list(map(int, input().split())) for _ in range(n)]
    visit = [0]*n
    min_v = float('inf')
    sol(0,0)
    print(f'#{tc+1} {min_v}')