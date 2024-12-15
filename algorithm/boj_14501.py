import sys

input = sys.stdin.readline

def recur(idx, money):
    global max_v

    if idx >= n+1:
        max_v = max(max_v,money)
        return

    if idx+t[idx] <= n+1:
        # 상담 하는 경우
        recur(idx+t[idx], money+p[idx])
    # 상담 안하는 경우
    recur(idx+1,money)

n = int(input())

t = [ i for i in range(n+1)]
p = [ i for i in range(n+1)]

for i in range(1,n+1):
    ti, pi = map(int,input().split())
    t[i],p[i] = ti, pi

max_v = float('-inf')

recur(1,0)

print(max_v)