import sys
sys.stdin = open('16584_input.txt')
sys.stdout = open('16584_output.txt','w')

def f(i, k, s): # i-1까지 선택한 원소의 합
    global min_v
    if i==k:
        if min_v > s:
            min_v = s
    elif s>=min_v:
        return
    else:
        for j in range(i,k): # p[i] 자리에 올 원소 p[j]
            p[i],p[j] = p[j],p[i] # p[i]<->p[j]
            f(i+1, k, s+arr[i][p[i]])
            p[i],p[j] = p[j],p[i] # 원상복구

for tc in range(int(input())):
    n=int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    min_v = 100
    f(0, n, 0) #(시작위치, 총 갯수)
    print(f'#{tc+1} {min_v}')
