import sys
input = sys.stdin.readline

# 각 줄이 최소 1개 최대 15개 글자가 주어진다고 했으니 15*5배열 생성
board = [[0 for _ in range(15)] for _ in range(5)]

arr = []

for i in range(5):
    text = list(map(str,input().rstrip()))
    len_text = len(text)
    
    for j in range(len_text):
        board[i][j] = text[j]

for i in range(len(board)):
    for j in range(len(board)):
        if board[j][i] == 0:
            continue
        else:
            print(board[j][i],end='')