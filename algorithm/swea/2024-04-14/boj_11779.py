import sys,heapq
input = sys.stdin.readline
INF = int(1e9)

def sol(start):
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] <= dist:
            if distance[now] == dist:
                
            else:
                continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n = int(input())
m = int(input())

graph = [[]for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start,end = map(int,input().split())

sol(start)

result = []
for i in range(1, n+1):
    if distance[i] == distance[end]: 
        result.append(i)



print(distance[end])
print(f'dist: {distance}')
print(result)