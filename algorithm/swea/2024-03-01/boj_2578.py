import sys
from collections import deque
input = sys.stdin.readline

def check_bingo():
    bingo = 0
    for i in range(5):
        if sum(arr[i]) == 0:
            bingo+=1
    # 열
    for j in range(5):
        sum_v = 0
        for i in range(5):
            sum_v+=arr[i][j]
        if sum_v == 0:
            bingo+=1
    # 대각선
    temp1 = arr[0][4] + arr[1][3] + arr[2][2] + arr[3][1] + arr[4][0]
    temp2 = arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4]
    if temp1 == 0:
        bingo+=1
    if temp2 == 0:
        bingo+=1

    return bingo
arr = [list(map(int,input().split())) for _ in range(5)]
commands = deque(list(map(int,input().split())) for _ in range(5))
cnt=0

while commands:
    command = commands.popleft()

    for num in command:
        for row in arr:
            if num in row:
                row[row.index(num)]=0
                cnt+=1
            if cnt>=12:
                if check_bingo()>=3:
                    print(cnt)
                    exit()


