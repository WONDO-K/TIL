import sys
sys.stdin = open('18620_input.txt')
sys.stdout = open('18620_output.txt', 'w')


def bfs(start):
    global cnt
    que = [start]
    idx = 0
    while que:
        now = que[idx]
        if now == m:
            return visit[now]
        for num in [now+1,now-1,now*2,now-10]:
            if 1<=num<1000001 and not visit[num]:
                visit[num] = visit[now]+1
                que.append(num)
        idx+=1


for tc in range(int(input())):
    n,m = map(int,input().split())
    visit=[0]*1000001
    print(f'#{tc+1} {bfs(n)}')
