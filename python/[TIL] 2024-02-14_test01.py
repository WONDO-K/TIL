def f(i,k,target): # k개의 원소를 가진 배열A, 부분 집합의 합이 t인 경우
    if i==k: # 모든 원소에 대해 결정하면(부분집합이 완성되는 부분)
        ss = 0 # 부분 집합의 합
        for j in range(k):
            if bit[j]: # A[j]가 포함된 경우
                ss += A[j]
        if ss == target: # 부분집합의 합이 target인 경우
            for j in range(k):
                if bit[j]: # A[j]가 포함된 경우
                    print(A[j], end= ' ')
            print()
    else:
        for j in range(1,-1,-1):
            bit[i]=j
            f(i+1,k,target)
        # bit[i]=1
        # f(i+1,k)
        # bit[i]=0
        # f(i+1,k)

N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*N # bit[i] = A[i]의 포함여부를 결정한다.
f(0,N,16)
