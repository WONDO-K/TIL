import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    temp = [0]*len(arr[i])
    for j in range(len(arr[i])):
        if arr[i][j]=='O':
            if j==0:
                temp[j]=1
            else:
                temp[j] = temp[j-1]+1
    print(sum(temp))

