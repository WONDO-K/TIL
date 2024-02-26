# import sys
# sys.stdin = open('algo2_sample_in.txt')
# sys.stdout = open('algo2_sample_out.txt','w')

def solve(row,col,sum_v):
    global max_v

    if col == n: # 열의 선택이 모두 끝났다면
        max_v = max(max_v,sum_v)
    elif max_v>sum_v: # max_v가 sum_v보다 큰 경우는 어차피 갱신이 되지 않으므로 아래의 재귀 호출 단계를 진행하지 않고 그냥 return 처리
        return
    else:
        for i in range(n):
            if not row[i]: # 선택하지 않은 행이라면
                # 음수 과녁은 맞추면 안되기 때문에 양수일 때만 재귀호출, 조건상 점수는 1이상 50이하로 주어지기 때문에
                # 0 초과 범위로 설정해도 무관하다
                if arr[i][col]>0: 
                    row[i] = True
                    solve(row,col+1,sum_v+arr[i][col])
                    row[i] = False


for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    row_check = [False]*n
    max_v = -float('inf')
    solve(row_check,0,0)

    print(f'#{tc+1} {max_v}')
