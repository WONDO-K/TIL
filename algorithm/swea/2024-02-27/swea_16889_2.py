import sys
sys.stdin = open('16889_input.txt')
sys.stdout = open('16889_output.txt','w')


def dfs(cnt,sum_v,start):
    global min_v
    
    if cnt == n:
        min_v = min(min_v,sum_v + arr[start][0])# 시작점으로 돌아가는 값
    if sum_v > min_v:
        return
    for i in range(1,n): # 0에서 1로 가는 것은 1에서 출발하는 것과 같다
        if visit[i]==0 and arr[start][i]!=0: # 각 사물함을 돌기 때문에 ex)2->2는 없겠지만
            visit[i] = 1
            dfs(cnt+1,sum_v+arr[start][i],i)
            visit[i] = 0

for tc in range(int(input())):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visit = [0]*n
    min_v = float('inf')
    dfs(1,0,0) #0->1 은 1에서 출발하는 것과 같기 때문에 cnt를 1로 시작한다.
    print(f'#{tc+1} {min_v}')



