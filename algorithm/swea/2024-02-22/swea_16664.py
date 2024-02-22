import sys
sys.stdin = open('16664_input.txt')
sys.stdout = open('16664_output.txt', 'w')

for tc in range(int(input())):
    a = float(input())
    result=''
    while True:
        if a == 1:
            result+='1'
            break
        else:
            a = a*2
            if a>1:
                a-=1
                result+='1'
            elif a<1:
                result+='0'

    print(f'#{tc+1} ',end='')
    if len(result)>13:
        print('overflow')
    else:
        print(''.join(result))