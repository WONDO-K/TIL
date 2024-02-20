import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

def solve(x,y):

    start = arr[x][y]
    old_x, old_y = x,y
    cnt=0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == start and (old_x<i and old_y<j):
                return cnt
            else:
                cnt+=1



T = int(input())

for tc in range(T):
    arr = []
    N = int(input())

    for _ in range(N):
        arr.append(list(map(int,input().split())))

    result = []
    for i in range(N):
        for j in range(N):
            result.append(solve(i,j))


    print(result)