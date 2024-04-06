import sys
input=sys.stdin.readline

k,n = map(int,input().split())

rope = []

for _ in range(k):
    rope.append(int(input()))
rope.sort()

start,end = 1, max(rope)
result= 0
while start<=end:

    mid = (start+end)//2
    cnt = 0
    for i in rope:
        cnt += i//mid

    if cnt >= n:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)