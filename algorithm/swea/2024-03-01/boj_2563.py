import sys
input = sys.stdin.readline

n = int(input())

board = [[0 for _ in range(101)] for _ in range(101)]
arr = []

for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])


for col,row in arr:
    for i in range(row,row+10):
        for j in range(col,col+10):
            if board[i][j]==0:
                board[i][j]=1
cnt=0
for i in board:
    cnt+=i.count(1)
print(cnt)