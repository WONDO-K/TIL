import sys
import math
import heapq

input = sys.stdin.readline
INF = math.inf

def sol(start):
    q = []
    move = 0
    heapq.heappush(q,(0,start))
    cnt[start] = 0

    while q:
        move,now = heapq.heappop(q)
        if move > cnt[now]:
            continue
        for next in arr[now]:
            new_move = next[1]+move
            if move < cnt[next[0]]:
                cnt[next[0]] = new_move
                heapq.heappush(q,(new_move,next[0]))




n,m,k,x = map(int,input().split())
cnt = [INF]*(n+1)
arr = [[] for _ in range(n+1)]
result=[]


for i in range(m):
    start,end = map(int,input().split())
    arr[start].append((end,1))
sol(x)

for i in range(1, n+1):
    if cnt[i] == k: 
        result.append(i)

if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)