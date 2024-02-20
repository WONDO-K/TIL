import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    t,N = map(str,input().split())
    N = int(N)
    arr = []
    arr.append(list(map(str,input().split())))
    temp = [[]for i in range(10)]
    standard = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in arr[0]:
        temp[standard.index(i)].append(i)
    print(f'#{tc+1}')
    for i in temp:
        print(' '.join(i))