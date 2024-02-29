import sys
sys.stdin = open('2117_input.txt')
sys.stdout = open('2117_output.txt', 'w')

for tc in range(int(input())):
    # n:도시의 크기, m: 하나의 집이 지불 가능한 비용
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_cnt = -float('inf')
    for k in range(1,n+2):
        cost = k**2 + (k-1)**2
        for i in range(n):
            for j in range(n):
                cnt=0
                for row in range(-(k-1),(k-1)+1):
                    for col in range(-((k-1)-abs(row)),(k-1)-abs(row)+1):
                        if 0<=i+row<n and 0<=j+col<n:
                            cnt += arr[i+row][j+col]
                if cnt*m-cost>=0:
                    max_cnt=max(max_cnt,cnt)
    print(f'#{tc+1} {max_cnt}')