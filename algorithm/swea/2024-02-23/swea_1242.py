import sys
sys.stdin = open('1242_input.txt')
sys.stdout = open('1242_output.txt', 'w')

for tc in range(int(input())):
    n,m = map(int,input().split())

    arr = []
    for i in range(n):
        temp = input().strip('0')
        print(temp)
        if len(temp) != 0:
            if len(temp)>15:
                temp2 = list(temp.split('0'))
                print(temp2)
                # temp2=[]
                # print(temp[-15:])
                # temp2.append(temp[-15:])
                # idx=-16
                # while True:
                #     print(idx)
                #     print(temp[idx])
                #     if temp[idx]=='0':
                #         idx-=1
                #     else:
                #         temp2.append(temp[idx-16:idx])
                #         break
                # arr.append(temp2)
            else:
                arr.append(temp)


    if tc+1==2:
        for i in arr:
            print(i)
