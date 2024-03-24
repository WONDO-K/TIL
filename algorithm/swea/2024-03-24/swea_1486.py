import sys

sys.stdin = open('1486_input.txt')


def dfs(depth, sum_v):
    global max_v

    print(f'max_v : {max_v}, sum_v :{sum_v}')

    if sum_v >= b:
        print(f'>=b : {sum_v}')
        max_v = min(max_v, sum_v)
        return

    # 모든 점원을 활용했는가? (쌓기 or 쌓지 않기의 경우를 모두 고려했는가)
    if depth == n:
        return

    # 이 문제에서 모든 종합원의 키를 합치면 1,3,3,5,6=> 18 이상의 값은 나오지 않는다.
    # 사용 하나 안하나 똑같지 않나 싶음
    # if sum_v>sum(arr):
    #     print(f'return max_v : {max_v}, sum_v :{sum_v}')
    #     return

    # depth는 i번째 점원을 뜻함
    # i번째 점원을 사용
    dfs(depth + 1, sum_v + arr[depth])

    # i번재 점원 미사용
    dfs(depth + 1, sum_v)


for tc in range(int(input())):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    # 높이가 b이상인 값들중에 가장 작은 값을 찾아야 하기 때문에 양의 무한대 사용
    max_v = float('inf')
    dfs(0, 0)
    print(f'#{tc + 1} {max_v - b}')


