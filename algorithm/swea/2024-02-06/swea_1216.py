import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(10):
    t = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(str, input())))
    cnt = 0

    for i in range(100):
        for j in range(100):
            for k in range(99,-1,-1):
                temp = arr[i][j:j+k]
                if temp == temp[::-1]:
                    cnt = max(cnt,len(temp))

    for k in range(99,-1,-1):
        for i in range(100):
            for j in range(100-k):
                s = ''
                for t in range(k):
                    s = s+str(arr[j+t][i])
                if s == s[::-1]:
                    cnt = max(cnt, len(s))

    print(f'#{tc+1} {cnt}')