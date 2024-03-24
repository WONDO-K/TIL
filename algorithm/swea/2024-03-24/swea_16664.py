import sys
sys.stdin = open('16664_input.txt')

for tc in range(int(input())):
    num = float(input())
    result = ''
    while True:
        if num == 1:
            result+='1'
            break
        else:
            num *= 2

            if num>1:
                num-=1
                result+='1'
            elif num<1:
                result+='0'

    if len(result)>=13:
        print(f'#{tc+1} overflow')
    else:
        print(f'#{tc+1} {result}')
