import sys
sys.stdin = open('1486_input.txt')

from itertools import combinations

for tc in range(int(input())):
    n,b = map(int,input().split())
    arr = list(map(int,input().split()))

    result = []

    for i in range(1,n+1):
        nums = list(combinations(arr,i))
        for j in nums:
            sum_v = sum(j)
            if sum_v>=b:
                result.append(sum_v)
    result.sort()

    print(f'#{tc+1} {result[0]-b}')


