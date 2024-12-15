import sys

input = sys.stdin.readline

def recur(idx,weight,value):
    global max_v

    if idx == n:
        max_v = max(max_v, value)
        return
    
    # 담는 경우
    if weight+w[idx] <= k:
        recur(idx+1,weight+w[idx],value+v[idx])
    # 안담는 경우
    recur(idx+1,weight,value)

n,k = map(int,input().split())

w = [i for i in range(n)]
v = [i for i in range(n)]

for i in range(n):
    wi,vi = map(int,input().split())
    w[i],v[i] = wi, vi
    
max_v = float('-inf')
recur(0,0,0)
print(max_v)