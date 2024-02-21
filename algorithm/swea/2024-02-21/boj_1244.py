import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
student = int(input())
arr.insert(0,0)

for _ in range(student):
    gender,num = map(int,input().split())

    if gender == 1:
        for i in range(1,len(arr)):
            if i%num==0:
                arr[i]=arr[i]^1

    else:
        if num < n//2:
            limit = num-1
        else:
            limit = n-num
        for i in range(limit,0,-1):
            if arr[num-i:num+i+1] == arr[num-i:num+i+1][::-1]:
                for j in range(i,0,-1):
                    arr[num-j],arr[num+j] = arr[num-j]^1, arr[num+j]^1
                    break
        arr[num] = arr[num] ^ 1



for i in range(1,n+1):
    print(arr[i],end=' ')
    if i%20==0:
        print()

