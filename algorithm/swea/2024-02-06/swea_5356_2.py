import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):

    arr = []
    max_leng=0
    arr = [input() for _ in range(5)]
    max_leng = max([len(word) for word in arr])

    temp = [[0 for i in range(max_leng)] for i in range(5)]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp[i][j] +=1

    print(f'#{tc+1} ',end='')

    for j in range(max_leng):
        for i in range(len(arr)):
            if temp[i][j] != 0:
                print(arr[i][j],end='')
    print()


