import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

def get_col_sum(arr):
    return max(sum(arr[i]) for i in range(len(arr)))

def get_row_sum(arr):
    result=[]
    for j in range(100):
        sum_v = 0
        for i in range(100):
            sum_v+= arr[i][j]
        result.append(sum_v)

    return max(result)

def get_left_cross_sum(arr):
    sum_v = 0
    for i in range(100):
        sum_v+= arr[i][i]
    return sum_v

def get_right_cross_sum(arr):
    result=[]
    sum_v = 0
    x=0
    y=99
    for _ in range(100):
        sum_v += arr[x][y]
        x += 1
        y -= 1
    return sum_v

while True:
    T = input()
    arr = []
    for _ in range(100):
        arr.append(list(map(int,input().split())))


    result = []

    result.append(get_row_sum(arr))
    result.append(get_col_sum(arr))
    result.append(get_left_cross_sum(arr))
    result.append(get_right_cross_sum(arr))

    print(f'#{T} {max(result)}')

    if T == '10':
        break