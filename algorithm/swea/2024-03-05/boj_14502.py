import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
temp = [i for i in range(1,n*m+1)]
point = list(combinations(temp,3))


for i in range(7):
    for j in range(7):
        print(7 * i + j + 1, end=' ')
    print()

print(arr)
print(len(point))

