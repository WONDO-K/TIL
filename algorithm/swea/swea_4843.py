import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input()))

    check = [0]*10

    for i in range(N):
        check[num[i]]+=1

    result = 0
    idx=0
    for j in range(len(check)):
        if result<=check[j]:

            result=check[j]
            idx=j

    print("#%d %d %d" % (tc, idx, result))



