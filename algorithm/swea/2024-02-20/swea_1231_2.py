import sys
sys.stdin = open('1231_input.txt')
sys.stdout = open('1231_output.txt','w')

def in_order(idx):
    global num
    if idx<=n:
        return in_order(idx*2) + arr[idx] + in_order(idx*2+1)
    else:
        return ''


for tc in range(10):
    n = int(input())
    arr = [0 for i in range(n+1)]
    for i in range(1,n+1):
        arr[i] = input().split()[1]

    print(f'#{tc+1} {in_order(1)}')