import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N+1)]
for i in range(N-1) :
    A, B, C = map(int, input().split())
    lst[A].append((B, C))
    lst[B].append((A, C))
inf = float('inf')
dis = [0] + [inf] * (N)
# print(lst, dis)

def f(start) :
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if dist < dis[now] :
            continue
        for next_n, next_d in lst[now] :
            cost = dist + next_d
            if cost < dis[next_n] :
                dis[next_n] = cost
                heapq.heappush(q, (cost, next_n))

f(1)
ans = 0
for i in dis :
    if (i != inf) and ans < i :
        ans = i
print(ans)