def f(i, k, s, target): # k개의 원소를 가진 배열A, 부분 집합의 합이 t인 경우
    global cnt
    cnt+=1
    if s == target: # 목표치에 도달
        for j in range(k):
            if bit[j]: # A[j]가 포함된 경우
                print(A[j],end=' ')
        print()
    elif i == k: # 모든 원소를 고려했으나 s!=t
        return
    elif s > target: #고려한 원소의 합이 t보다 큰 경우
        return
    else:
        # for j in range(1,-1,-1):
        #     bit[i]=j
        #     f(i+1,k,target)
        bit[i]=1 # 포함
        f(i+1, k, s+A[i], target)
        bit[i]=0 # 미포함
        f(i+1, k, s, target)

N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*N # bit[i] = A[i]의 포함여부를 결정한다.
cnt=0
f(0, N, 0, 16)
print('cnt = ', cnt)