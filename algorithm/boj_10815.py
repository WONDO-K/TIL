import sys
input = sys.stdin.readline

def solve(idx,num):
    left,right = 0,n-1

    while left<=right:
        mid = (left+right)//2
        if arr[mid] == num:
            print('idx up')
            ans[idx]+=1
            return
        
        if arr[mid] < num:
            left = mid+1
        else:
            right= mid-1


n = int(input())

arr = sorted(list(map(int,input().split())))

m = int(input())
target = list(map(int,input().split()))
ans = [0] * m

for idx,num in enumerate(target):
     solve(idx,num)

print(*ans)