import sys
import math
import heapq

input = sys.stdin.readline
INF = math.inf

def sol(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        
        # 0번 다음위치, 1번 거리비용
        for next in arr[now]:
            cost = dist+next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))

s,e= map(int,input().split())
k = int(input())
arr = [[] for _ in range(s+1)]
distance = [INF]*(s+1)

for _ in range(e):
    u,v,w = map(int,input().split())
    arr[u].append((v,w))

sol(k)
for i in range(1, s + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i]) 