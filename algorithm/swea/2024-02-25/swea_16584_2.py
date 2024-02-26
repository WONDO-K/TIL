def dfs(index,SUM):
    global cnt
    cnt = cnt + 1

    global result

    if SUM > result: #가지 치기
        return


    if index == N:
        if SUM < result:
            result = SUM


    for n in range(N):
        if not visited[n]:
            visited[n] = True
            dfs(index+1,SUM + MAP[index][n])
            visited[n] = False

T = int(input())

for t in range(T):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    result = 10000

    dfs(0,0)

    print(f'#{t+1} {result}')