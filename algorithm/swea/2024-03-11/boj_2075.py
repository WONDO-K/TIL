import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr=[]

for _ in range(n):
    temp = map(int, input().split())
    if len(arr)==0:
        for i in temp:
            heapq.heappush(arr,i)
    else:
        for i in temp:
            if arr[0] < i:
                heapq.heappop(arr)
                heapq.heappush(arr, i)

print(arr[0])

#
# import heapq
#
# heap = []
# n = int(input())
#
# for _ in range(n):
#     numbers = map(int, input().split())
#     for number in numbers:
#         if len(heap) < n: # heap의 크기를 n개로 유지
#             heapq.heappush(heap, number)
#         else:
#             if heap[0] < number:
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, number)
# print(heap[0])
