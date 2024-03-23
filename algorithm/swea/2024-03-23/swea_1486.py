import sys
sys.stdin = open('1486_input.txt')

def dfs(depth,sum_v):
    global max_v
    if sum_v >= b:
        max_v = min(max_v,sum_v)
        return
    
    # 모든 점원을 활용했는가? (쌓기 or 쌓지 않기의 경우를 모두 고려했는가)
    if depth == n:
        return
    
    # depth는 i번째 점원을 뜻함
    # i번째 점원을 사용
    dfs(depth+1,sum_v+arr[depth])
    
    # i번재 점원 미사용
    dfs(depth+1,sum_v)

    

for tc in range(int(input())):
    n,b = map(int,input().split())
    arr = list(map(int,input().split()))
    # 높이가 b이상인 값들중에 가장 작은 값을 찾아야 하기 때문에 양의 무한대 사용
    max_v = float('inf')
    dfs(0,0)
    print(f'#{tc+1} {max_v-b}')


