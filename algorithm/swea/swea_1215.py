import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

def row_solve(limit):
    global cnt
    for temp in arr:
        for j in range(0,8-limit+1):
            if temp[j:j+limit] == list(reversed(temp[j:j+limit])):
                cnt+=1
def col_solve(limit):
    global cnt
    for i in range(len(arr)):
        for j in range(0,8-limit+1):
            temp = []
            for k in range(limit):
                temp.append(arr[j+k][i])
            if temp == list(reversed(temp)):
                cnt+=1

for tc in range(10):
    N = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(map(str,input())))
    cnt = 0
    row_solve(N)
    col_solve(N)
    print(f'#{tc+1} {cnt}')