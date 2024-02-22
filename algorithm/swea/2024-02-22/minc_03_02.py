import sys
sys.stdin = open('minc_03_input.txt')
sys.stdout = open('minc_03_output.txt', 'w')

for tc in range(int(input())):
    n, k =map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))

    result = 1
    idx=0
    for pc in passcode:
        if pc not in sample:
            result=0
            break
        idx=sample.index(pc)
        temp = sample[idx+1:n]
        sample = temp



    print(f'#{tc+1} {result}')
