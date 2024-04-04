import sys
input=sys.stdin.readline

n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:

    start,end = 0,n-1
    flag = 0
    while start<=end:
        mid = (start+end)//2

        if i == arr1[mid]:
            flag = 1
            print(1)
            break
        elif i > arr1[mid]:
            start = mid+1
        else:
            end = mid-1

    if flag == 0:
        print(0)
