n = int(input())
arr = [[0 for i in range(7)] for i in range(2)]
print(arr)

temp1=n
temp2=n
for i in range(0,4):
    arr[0][i]=temp1
    temp1+=1
for i in range(6,2,-1):
    arr[1][i] = temp2
    temp2-=1
print(arr)