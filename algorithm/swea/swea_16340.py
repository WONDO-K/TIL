import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):

    str1 = input()
    str2 = input()

    result=0

    if str1 in str2:
        result=1

    print(f'#{tc+1} {result}')