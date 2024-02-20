import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):

    arr = input()
    after = list(reversed(arr))
    flag = 1
    for i in range(len(arr)):
        if arr[i] != after[i]:
            flag=0
            break
        else:
            break
    print(f'#{tc+1} {flag}')



