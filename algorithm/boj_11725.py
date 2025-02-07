import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

graph = [[] for _ in range(n+1)]
par = [0 for _ in range(n+1)]
child_num = [0 for _ in range(n+1)] # 자식의 수 - 후위순회


for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def recur(node,prv):

    par[node] = prv

    for nxt in graph[node]:
        if nxt == prv: # 역주행 방지 코드
            continue
        recur(nxt,node)

    child_num[prv]+=1 # 이전 위치 prv가 부모임
recur(1,0)

for i in par[2:]:
    print(i)

print(child_num)