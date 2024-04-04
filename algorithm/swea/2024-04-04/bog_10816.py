import sys
input=sys.stdin.readline

n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()
result = {}

for i in arr1:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

m = int(input())
arr2 = list(map(int,input().split()))

for num in arr2:
    start,end = 0,n-1
    mid=0
    while start<=end:
        mid = (start+end)//2
        if num == arr1[mid]:
            break
        elif num > arr1[mid]:
            start = mid+1
        else:
            end = mid-1
    if num == arr1[mid]:
        print(result[num],end=' ')
    else:
        print(0,end=' ')
