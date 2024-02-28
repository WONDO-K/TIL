import sys
sys.stdin = open('2827_input.txt')
sys.stdout = open('2827_output.txt','w')


def get_sub(tar):
    global result
    temp = 0
    for i in range(n):
        if tar & 0x1:  # 1 비트가 1인지 확인
            temp+=int(arr[i])
        tar >>= 1
    if temp==k:
        result+=1

for tc in range(int(input())):
    n,k = map(int,input().split())
    arr = list(input().split())

    result=0
    for tar in range(1<<n):
        get_sub(tar)
    print(f'#{tc+1} {result}')