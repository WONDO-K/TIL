import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):

    arr = input()

    if arr != arr[::-1]:
        print(f'#{tc+1} {0}')
    else:
        print(f'#{tc+1} {1}')



