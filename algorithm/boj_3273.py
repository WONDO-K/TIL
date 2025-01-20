import sys

input = sys.stdin.readline


n = int(input())

arr = list(map(int,input().split()))
arr.sort()
x = int(input())

left,right = 0,n-1
cnt=0
# while left<right:
#     if arr[left]+arr[right] == x:
#         cnt+=1
#         left+=1
#         right-=1
#     else:
#         if arr[left]+arr[right] < x: # x보다 작은 경우 left를 올리면 값을 증가
#             left+=1
            
#         else: # x보다 큰 경우 right를 줄이면 값을 감소 시킨다는 의미
#             right-=1
while left<right:
    if arr[left] + arr[right] == x:
        cnt+=1
    
    if arr[left] + arr[right] >= x:
        right-=1
    else:
        left+=1
print(cnt)
