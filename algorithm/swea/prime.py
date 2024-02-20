import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    prime_num = [2,3,5,7,11]
    check =[0]*12

    point = 0
    while N!=1:
        if N % prime_num[point] !=0:
            point+=1
            if point>len(prime_num):
                break
        else:
            N//=prime_num[point]
            check[prime_num[point]]+=1
    result=[]
    for i in range(len(prime_num)):
        result.append(check[prime_num[i]])

    print(f'#{tc} ',end='')
    print(*result)


