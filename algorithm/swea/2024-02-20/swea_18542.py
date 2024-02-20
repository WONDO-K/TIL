import sys
sys.stdin = open('18542_input.txt')
sys.stdout = open('18542_output.txt','w')

def in_order(idx):
    global num
    if idx > n:
        return
    else:
        in_order(idx*2)
        arr[idx] = num
        num+=1
        in_order(idx*2+1)


for tc in range(int(input())):
    n = int(input())
    arr=[0 for i in range(n+1)]
    num=1
    in_order(1)
    print(arr)
    print(f'#{tc+1} {arr[1]} {arr[n//2]}')
