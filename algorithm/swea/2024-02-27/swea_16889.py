import sys
from itertools import permutations
sys.stdin = open('16889_input.txt')
sys.stdout = open('16889_output.txt','w')

def solve(lst):
    global min_v
    # 1을 제외하고 경로의 순서를 만들었기 때문에
    # 하드코딩으로 1에서 제일 처음 목적지로 가는 소비량을 더해주고 시작한다.
    # 그리고 j 위치에 -1을 해준 이유는 그림상 시작점이 1,1 이지만 배열의 인덱스상 0,0에서 시작하기 떄문에
    # 1씩 줄여준다.
    sum_v = arr[0][lst[0]-1]
    for i in range(1,len(lst)):
        sum_v+=arr[lst[i-1]-1][lst[i]-1] # 해당 위치도 1을 빼준 이유는 동일하다.

    # 가장 마지막은 출발점인 1,1(즉,[0,0])으로 돌아오는 것 또한 고정이기 때문에
    # 출발 시에 소비량을 하드코딩 해준 것처럼 시작점으로 돌아가는 소비량 또한 하드코딩으로 더 해준다.
    sum_v += arr[lst[-1]-1][0]

    return sum_v

for tc in range(int(input())):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 1의 위치는 고정이기 때문에 2~n까지의 숫자를 순열을 통해 순회한다.
    # n이 5일때 1을 제외한 2,3,4,5를 가지고 순열을 만들기 때문에
    # 4가지 숫자로 조합을 만든다는 의미로 n-1개의 원소를 가진 순열을 생성한다.
    route = list(permutations([i for i in range(2,n+1)],n-1))

    min_v = float('inf')
    # 순열을 통해 만든 경로의 순서의 모음을 각 한개씩 통째로 solve에 삽입한다.
    for i in route:
        min_v = min(min_v,solve(i)) # solve에서 return한 합계 비교후 작은 값 저장
    print(f'#{tc+1} {min_v}')



