import sys
import heapq

input = sys.stdin.readline

def djk(start):

    que = []
    heapq.heappush(que,(0,start))
    distance[start]=0


    while que:
        # 우선순위 큐를 이용해서, 거리를 보고 정렬한다.
        dist, now = heapq.heappop(que)

        if dist > distance[now]:
            continue

        for nxt, value in arr[now]:
            if distance[now]+value < distance[nxt]:
                distance[nxt] = distance[now] + value
                heapq.heappush(que,(distance[nxt],nxt))


n,m = map(int,input().split())
start = int(input())

arr = [[]for _ in range(n+1)]

for _ in range(m):
    s,e,v = map(int,input().split())
    arr[s].append((e,v))


distance = [1e9] * (n+1)  
djk(start)

for i in range(1,n+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])