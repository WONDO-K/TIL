import sys
sys.stdin = open('18132_input.txt')
sys.stdout = open('18132_output.txt','w')


def f(i, k, s, target): # k개의 원소를 가진 배열A, 부분 집합의 합이 t인 경우
    global cnt
    if s == target and i==k: # 목표치에 도달
        temp = 0
        for j in range(k):
            if bit[j]: # A[j]가 포함된 경우
                temp+=1
        if temp == N:
            cnt+=1
    elif i == k: # 모든 원소를 고려했으나 s!=t
        return
    elif s > target: #고려한 원소의 합이 t보다 큰 경우
        return
    else:
        bit[i]=1 # 포함
        f(i+1, k, s+A[i], target)
        bit[i]=0 # 미포함
        f(i+1, k, s, target)


for tc in range(int(input())):
    N, target = map(int, input().split())
    A = [i for i in range(1, 13)]  # 수정된 부분
    bit = [0] * 12  # bit[i] = A[i]의 포함여부를 결정한다.
    cnt = 0
    f(0, 12, 0, target)

    print(f'#{tc + 1} {cnt}')