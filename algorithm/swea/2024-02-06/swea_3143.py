import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):

    A, B = input().split()
    cnt = 0

    idx = 0
    len_a = (len(A))
    len_b = len(B)
    while True:
        if idx > len_a - 1:
            break
        else:
            temp = A[idx:idx + len(B)]
            if temp == B:
                cnt += 1
                idx += (len(B))
            else:
                cnt += 1
                idx += 1
    print(f'#{tc + 1} {cnt}')

