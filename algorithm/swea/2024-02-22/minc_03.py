import sys
sys.stdin = open('minc_03_input.txt')
sys.stdout = open('minc_03_output.txt', 'w')

for tc in range(int(input())):
    n, k =map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))

    result = 1

    for i in range(k):
        if passcode[i] not in sample:
            result = 0
            break

        print(f'passcode = {passcode[i]}')
        idx = sample.index(passcode[i])
        print(f'idx : {idx}')

        while True:
            if sample[idx]==passcode[i]:
                break
            else:
                idx+=1
        print(f'after : {idx}')
        temp = sample[idx:n]
        print(f'temp : {temp}')
        for j in range(i,n):
            #print(f'j : {j}')
            if passcode[j] not in temp:
                result=0
                break

    print(f'#{tc+1} {result}')
