import sys
import math
import heapq

input = sys.stdin.readline
INF = math.inf


def sol(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0

    while q:
        dis,now = heapq.heappop(q)
        # 지금 꺼낸 거리가 dist에 담겨 있는 거리 정보보다 크면 고려 대상이 아님
        if dis > dist[now]:
            continue

        for i in arr[now]:
            new_cost = dis+i[1]

            # dist에 저장된 거리값보다 낮은 값이라면 
            if new_cost < dist[i[0]]:
                dist[i[0]] = new_cost
                heapq.heappush(q,(new_cost,i[0]))

n,d = map(int,input().split())
arr = [[] for _ in range(d+1)]
dist = [INF]*(d+1)

# ex 1 -> 2 가는 거리비용이 1이라는 의미
# 0번 : 목적지, 1번 비용
for i in range(d):
    arr[i].append((i+1,1))

# ex) 0->50 루트의 지름길이 있다면 0의 종착지를 1이 아닌 50으로 업데이트 해준다.
for _ in range(n):
    s,e,cost = map(int,input().split())
    if e>d:
        continue
    arr[s].append([e,cost])
sol(0)

print(dist[d])