import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())
for tc in range(T):
    N,Q = map(int,input().split())
    result = [0 for i in range(1, N + 1)]

    for q in range(1,Q+1):
        L,R = map(int,input().split())
        for i in range(L,R+1):
            result[i-1] = q



    print(f"#{tc+1} {' '.join(map(str,result))}")