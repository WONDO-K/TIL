import sys
sys.stdin = open('18621_input.txt')
sys.stdout = open('18621_output.txt', 'w')


def dfs(start):
    visit[start]=1

    for next in arr[start]:
        if visit[next] == 0:
            dfs(next)
    return



for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    visit = [0] * (n + 1)
    pair = list(map(int,input().split()))

    for i in range(0,len(pair),2):
        a,b = pair[i],pair[i+1]
        arr[a].append(b)
        arr[b].append(a)

    cnt=0
    for i in range(1,n+1):
        if not visit[i]:
            dfs(i)
            cnt+=1
    print(f'#{tc+1} {cnt}')