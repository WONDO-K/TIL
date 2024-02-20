import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())
for tc in range(T):
    D, A, B, F = map(int,input().split())

    time = D/(A+B)
    result = time*F

    print(f'#{tc+1} {result}')