import sys
sys.stdin = open('1238_input.txt')
sys.stdout = open('1238_output.txt','w')

from collections import deque

def bfs(start):
    global limit
    que = deque()
    que.append((1,start))
    visit[start]=1
    temp=[]
    while que:
        cnt,next = que.popleft()
        for i in phone[next]:
            if visit[i]==0:
                visit[i]=1
                que.append((cnt+1,i))
                temp.append((cnt+1,i))
    limit = max(a[0] for a in temp)
    return temp


for tc in range(10):
    n,s = map(int,input().split())

    arr = list(map(int,input().split()))
    phone = [[]for _ in range(101)]
    visit = [0 for _ in range(101)]
    limit = 0

    for i in range(n):
        if i%2==0:
            phone[arr[i]].append(arr[i+1])
    print(phone)
    temp = bfs(s)
    ans=-1
    for i in temp:
        if i[0]==limit:
            ans = max(ans,i[1])
    print(f'#{tc+1} {ans}')