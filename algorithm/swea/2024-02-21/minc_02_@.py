import sys
sys.stdin = open('minc_02_input.txt')
sys.stdout = open('minc_02_output.txt', 'w')

def sol():
    max_area=0
    max_area_cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(i,n):
                for z in range(j,n):
                    if arr[i][j] == arr[k][z]:
                        area = (k - i + 1) * (z - j + 1)
                        if area>max_area:
                            max_area = area
                            max_area_cnt = 1
                        elif area == max_area:
                            max_area_cnt+=1
    return max_area_cnt
for tc in range(int(input())):
    arr = []
    n = int(input())

    arr=[]

    for _ in range(n):
        arr.append(list(map(int,input().split())))

    print(f'#{tc+1} {sol()}')