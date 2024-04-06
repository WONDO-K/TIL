import sys
input=sys.stdin.readline

n,m = map(int,input().split())

tree = list(map(int,input().split()))
tree.sort()

start,end = 1,tree[-1]
#start,end = 1,max(tree)
# max에서 시간 복잡도를 손해봤음
# 정렬을 했기 때문에 tree의 가장 마지막 값이 큰 값이기 때문에 바로 사용하면 되는데 max를 쓰는 실수함
result = 0
while start<=end:
    mid = (start+end)//2
    cnt = 0
    for i in tree:
        if i>mid:
            cnt+= i-mid

    if cnt>=m:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)