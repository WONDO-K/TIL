import sys
import heapq
input = sys.stdin.readline

n = int(input())

zero_cnt=0
heap=[]
arr = []

for _ in range(n):
    arr.append(int(input()))

for num in arr:
    if num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)