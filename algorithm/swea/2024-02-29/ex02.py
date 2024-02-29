import sys
sys.stdin = open('ex02_input.txt')
sys.stdout = open('ex02_output.txt','w')

def get_sero_cnt(col):
    cnt=0
    #red 자성체 체크
    is_red = False
    
    for row in range(n):
        # 1. red 자성체 발견
        if arr[row][col] == 1:
            is_red=True
        # 2. 이전에 red 자성체 발견, 현재 blue 자성체 발견 cnt+1
        elif is_red and arr[row][col]==2:
            cnt+=1
            is_red=False
    return cnt
for tc in range(10):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for col in range(n):
            ans+=get_sero_cnt(col)
    print(f'#{tc + 1} {ans}')
