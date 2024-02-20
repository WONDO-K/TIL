import sys
from collections import deque
sys.stdin = open('16636_input.txt')
sys.stdout = open('16636_output.txt','w')

for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int, input().split()))
    for i in range(m):
        arr.append(arr.pop(0))
    print(f'#{tc+1} {arr[0]}')