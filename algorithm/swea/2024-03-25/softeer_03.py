import sys
sys.stdin = open('03_input.txt')
sys.setrecursionlimit(10**6)

def dfs(now, arr1, visit):

    if visit[now] == 1: # 이미 방문 했다면
        return
    visit[now] = 1
    for neighbor in arr1[now]:
        dfs(neighbor,arr1,visit)
    return

for tc in range(int(input())):
    n,m = map(int,input().split())

    arr1 = [[] for _ in range(n+1)]
    arr2 = [[] for _ in range(n + 1)]
    for _ in range(m):
        x,y = map(int,input().split())
        arr1[x].append(y)
        arr2[y].append(x)
    s,t = map(int,input().split())

    fromS = [0] * (n+1)
    fromS[t] = 1 # 도착지를 방문처리하여 더이상 움직이지 못하게 함
    dfs(s,arr1,fromS)
    fromT = [0] * (n+1)
    fromT[s] = 1 # 출발지를 방문처리하여 더이상 움직이지 못하게 함
    dfs(t,arr1,fromT)
    
    # 역순 배열
    toS = [0] * (n+1)
    dfs(s,arr2,toS)
    toT = [0] * (n+1)
    dfs(t,arr2,toT)

    cnt = 0

    for i in range(1,n+1):
        if fromS[i] and fromT[i] and toS[i] and toT[i]:
            cnt+=1
    # 출발지, 도착지 모두 들리기 떄문에 2를 빼준다.
    print(cnt-2)
