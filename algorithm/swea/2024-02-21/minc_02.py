import sys
sys.stdin = open('minc_02_input.txt')
sys.stdout = open('minc_02_output.txt', 'w')

T = int(input())

def sol(start_i,start_j):
    global max_area,cnt
    target = arr[start_i][start_j]
    area=0
    for i in range(n):
        for j in range(n):
            if target == arr[i][j]:
                print(f'i:{i}, j:{j}')
                row = i-start_i+1
                col = j-start_j+1
                area = row*col
                print(f'row:{row},col:{col},area:{area}')
            if area > max_area:
                max_area = area
                cnt=1
            elif area == max_area:
                cnt+=1

for tc in range(T):
    arr = []
    n = int(input())

    arr=[]

    for _ in range(n):
        arr.append(list(map(int,input().split())))
    max_area = -1
    cnt=0
    for i in range(n):
        for j in range(n):
            sol(i,j)
    print(f'#{tc+1} max_area : {max_area}')
    print(f'cnt : {cnt}')

