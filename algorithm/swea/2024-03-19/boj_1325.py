import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    visit = [0] * (n + 1) # 중복된 컴퓨터를 감염시키는 경우 1번만 카운트해야 함(이걸 놓쳐서 메모리 초과 남)
    visit[i] = 1
    cnt=0
    while que:
        idx = que.popleft()
        # if len(arr[idx])!=0: # 현재 컴퓨터를 신뢰하는 컴퓨터로 이동시 아무 컴퓨터도 없다면 que추가 하지 않아야함
        for com in arr[idx]:
            if not visit[com]:
                que.append(com)
                visit[com]=1
                cnt+=1

    return cnt


n,m = map(int,input().split())

arr = [[] for _ in range(n+1)]


max_cnt = 1
scores = []

for _ in range(m):
    a,b = map(int,input().split())
    #arr[a].append(b)
    arr[b].append(a)

for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        scores = []
        scores.append(i)
    elif cnt == max_cnt:
        scores.append(i)

print(*scores)
