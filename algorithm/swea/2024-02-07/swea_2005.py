import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    N = int(input())

    arr = [[]for i in range(4)]
    arr[0].append(1)
    arr[1].append(1)
    arr[1].append(1)

    for i in range(2,N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i].append(1)
            else:
                temp = arr[i-1][j]+arr[i-1][j-1]
                arr[i].append(temp)
    print(f'#{tc+1}')
    for i in arr:
        print(*i)
