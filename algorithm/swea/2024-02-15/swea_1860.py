import sys
from collections import deque
sys.stdin = open('1860_input.txt')
sys.stdout = open('1860_output.txt','w')

# for tc in range(int(input())):
#     n,m,k = map(int,input().split())
#     arr = list(map(int,input().split()))
#     arr.sort()
#     time = [k if i%m == 0 and i!=0 else 0 for i in range(max(arr)+1)]
#     print(time)
#     flag = False
#     for i in arr:
#         #print(f'i : {i}, time[{i}]:{time[i]}')
#         if time[i]==0:
#             #print(f'time[{i-1}] : {time[i-1]}')
#             if time[i-1] == 0:
#                 #print(f'>0')
#                 flag=False
#                 break
#             elif time[i-1]>0:
#                 time[i-1]-=1
#                 flag = True
#         elif time[i]>=1:
#             time[i]-=1
#             flag = True
#
#     if flag == True:
#         print(f'#{tc+1} Possible')
#     else:
#         print(f'#{tc + 1} Impossible')
#
for tc in range(int(input())):
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()

    result = 'Possible'
    time = m

    for i in range(1,n+1,k):
        if arr[i-1]<time:
            result = 'Impossible'
            break
        time+=m
    print(f'#{tc+1} {result}')



