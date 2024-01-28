import sys
import math

input = sys.stdin.readline
INF = math.inf

def solve(point,x,y,abs_distance):

    for i in point:
        currnet_x = i[0]
        currnet_y = i[1]

        if min(x,x+abs_distance)<=currnet_x<=max(x,x+abs_distance) and (currnet_y==y or currnet_y==y+abs_distance):
            continue
        elif (currnet_x==x or currnet_x==x+abs_distance) and min(y,y+abs_distance<=currnet_y<=max(y,y+abs_distance)):
            continue
        else:
            return False
    else:
        return True



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

abs_distance = max(max_x-min_x,max_y-min_y)

if solve(point,min_x,min_y,abs_distance) or solve(point,min_x,max_y,abs_distance) or solve(point,max_x,min_y,abs_distance) or solve(point,max_x,max_y,-abs_distance):
    print(abs_distance)
else:
    print(-1)



