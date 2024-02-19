def f(i, k, s): # i-1까지 선택한 원소의 합
    global min_v, cnt
    cnt+=1
    if i==k:
        #print(*p)
        # s = 0 # 선택한 원소의 합
        # for j in range(k): # j행에 대해
        #     s+=arr[j][p[j]] # j행에서 p[j]열을 고른 경우의 합 구하기 
        if min_v > s:
            min_v = s
    elif s>=min_v:
        return
    else:
        for j in range(i,k): # p[i] 자리에 올 원소 p[j]
            p[i],p[j] = p[j],p[i] # p[i]<->p[j]
            f(i+1, k, s+arr[i][p[i]])
            p[i],p[j] = p[j],p[i] # 원상복구
n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
p = [i for i in range(n)]
min_v = 100
cnt=0
f(0, n, 0) #(시작위치, 총 갯수)
print(min_v,cnt)

