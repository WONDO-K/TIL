import sys
sys.stdin = open('ex01_input.txt')
sys.stdout = open('ex01_output.txt','w')

for tc in range(int(input())):
    n,m,k = map(int,input().split())
    client = list(map(int,input().split()))
    client.sort()
    result = 'Possible'
    limit = m
    for i in range(1,n+1,k):
        if client[i-1]<limit:
            result = 'Impossible'
            break
        limit+=m
    print(f'#{tc+1} {result}')

