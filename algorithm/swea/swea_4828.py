import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {max(arr)-min(arr)}')

