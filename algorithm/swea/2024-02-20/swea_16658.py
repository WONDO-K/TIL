import sys
sys.stdin = open('16658_input.txt')
sys.stdout = open('16658_output.txt','w')

def order(idx):
    global cnt

    if len(arr[idx])==0:
        return

    for next in arr[idx]:
        cnt+=1
        order(next)


for tc in range(int(input())):

    e,n = map(int,input().split())
    temp = list(map(int,input().split()))
    arr = [[]for i in range(e+2)]

    for i in range(0,len(temp),2):
        arr[temp[i]].append(temp[i+1])

    cnt=1
    order(n)
    print(f'#{tc+1} {cnt}')