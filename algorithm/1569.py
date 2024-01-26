import sys, math
input = sys.stdin.readline
INF = math.inf

n=int(input())

point = []


min_x = INF
min_y = INF
max_x = -(INF)
max_y = -(INF)

for i in range(n):
    a,b = map(int,input().split())
    point.append([a,b])

    if a < min_x:
        min_x = a
    if a > max_x:
        max_x = a
    if b < min_y:
        min_y = b
    if b > max_y:
        max_y = b

print(min_x, max_x, min_y, max_y)


# for current_x, current_y in point:
#     for i in range():


