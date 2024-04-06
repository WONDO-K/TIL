import sys
input=sys.stdin.readline


def cnt_rope(mid):
    cnt = 0
    for i in rope:
        cnt += i//mid
    return cnt

def sol(start,end):
    if start > end:
        return end

    mid = (start+end)//2

    cnt = cnt_rope(mid)

    if cnt >= n:
        return sol(mid+1,end)
    else:
        return sol(1,mid-1)


k,n = map(int,input().split())

rope = []

for _ in range(k):
    rope.append(int(input()))

start,end = 1, max(rope)

print(sol(start,end))


