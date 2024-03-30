import sys
input = sys.stdin.readline

def dfs(num):
    global result
    if len(arr) == 2:
        if result < num:
            result = num
        return
    for i in range(1,len(arr)-1):
        temp = arr[i]
        del arr[i]
        dfs(num+arr[i-1]*arr[i])
        arr.insert(i,temp)


n = int(input())
arr =list(map(int, input().split()))
result = 0
dfs(0)
print(result)