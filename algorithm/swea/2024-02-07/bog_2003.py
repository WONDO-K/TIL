n,m = map(int,input().split())
arr = list(map(int,input().split()))
temp = [0]*n
print(temp)
temp[0] = arr[0]
print(temp)
result=0
for i in range(1,len(arr)):
    temp[i] = temp[i-1]+arr[i]

