import sys
sys.stdin = open('1240_input.txt')
sys.stdout = open('1240_output.txt', 'w')

password = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

for tc in range(int(input())):
    n,m = map(int,input().split())

    arr=[]
    for i in range(n):
        temp = input().rstrip('0')
        if len(temp)!=0:
            arr.append(temp[-56:])

    code = arr[0]
    trans = []
    for i in range(0,len(code),7):
        trans.append(password[code[i:i+7]])



    temp1,temp2 = 0,0
    for i in range(len(trans)):
        if i%2==0:
            temp1+=int(trans[i])
        elif i%2==1:
            temp2+=int(trans[i])
    ans = (temp1*3)+temp2

    print(f'#{tc + 1} ',end='')
    if ans % 10 == 0:
        print(sum(trans))
    else:
        print(0)