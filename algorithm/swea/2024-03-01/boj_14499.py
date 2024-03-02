import sys
input = sys.stdin.readline
# n:세로,m:가로, x,y:좌표, k:명령 횟수
n,m,x,y,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
command = list(map(int,input().split()))

