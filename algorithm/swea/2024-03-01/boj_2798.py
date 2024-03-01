import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
result = []

max_v = -float('inf')

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k] <= m:
                max_v = max(max_v,arr[i]+arr[j]+arr[k])

print(max_v)
