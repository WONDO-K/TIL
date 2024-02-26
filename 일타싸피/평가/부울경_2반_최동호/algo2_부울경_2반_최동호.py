def solve(total_sum):
    global current_max
    x,y=0,0
    temp = (arr[0][0])
    while True:
        for i in range(x,x+(m-x)):
            for j in range(y,y+(m-y)):
                if current_max<arr[i][j]:
                    current_max = arr[i][j]
                    x,y=i,j

        if current_max == temp:
            break
        else:
            temp=current_max
        total_sum+=current_max
    return total_sum


for tc in range(int(input())):
    n,m = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]
    current_max = -float('inf')
    total_sum = solve(0)

    print(f'#{tc+1} {total_sum}')