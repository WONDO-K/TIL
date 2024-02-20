import sys
sys.stdin = open('1231_input.txt')
sys.stdout = open('1231_output.txt','w')

def in_order(idx):
    global num
    if idx > n:
        return
    else:
        in_order(idx * 2)
        arr[idx] = num
        num += 1
        in_order(idx * 2 + 1)


for tc in range(10):
    n = int(input())
    arr = [[] for i in range(n+1)]
    result = [''] * (n + 1)
    result2 = [''] * (n + 1)
    num=1

    for i in range(n):
        temp = input().split()
        result[int(temp[0])]=temp[1]

    in_order(1)

    for idx,check in enumerate(arr):
        if idx != 0:
            result2[check] += result[idx]

    print(f'#{tc+1} ',end='')
    for i in range(1,n+1):
        print(result2[i],end='')
    print()