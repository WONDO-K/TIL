import sys
sys.stdin = open('1247_input.txt')
sys.stdout = open('1247_output.txt', 'w')

# 하 우
dx =[1,0]
dy =[0,1]
def sol(x,y,sum_v):
    global min_v

    if x==n-1 and y==n-1: # 도착했을 때
        min_v = min(min_v,sum_v) # 더 작은 값을 min_v에
        return
    for i in range(2): #하, 우 방향만 순회 (2번)
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            sum_v+=arr[nx][ny] # 다음 좌표의 값을 더하여 재귀 호출후
            sol(nx,ny,sum_v)
            sum_v-=arr[nx][ny] # 다음 방향의 좌표 값을 더하기 위해 원복


for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    min_v = float('inf')
    sol(0,0,arr[0][0])
    print(f'#{tc+1} {min_v}')