import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
s,e = 0,arr[-1]
ans = 0
while s<=e:
    mid = (s+e)//2
    sum = 0

    for i in arr:
        if i>mid:
            sum += i-mid

    if sum >= m: # >= 의 조건으로 찾아야 정확히 m인 값을 찾지 못해도 가장 큰 근사값을 얻을 수 있다. 즉, sum은 조건에 따라 m에 가깝게 줄거나, 늘어난다.
        ans=mid
        s = mid+1
    else:
        e = mid-1


    
print(ans)