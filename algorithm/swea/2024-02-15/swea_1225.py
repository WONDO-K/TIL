import sys
from collections import deque
sys.stdin = open('1225_input.txt')
sys.stdout = open('1225_output.txt','w')

from collections import deque
for tc in range(10):
    n = int(input())
    arr = deque(map(int,input().split()))
    i=1
    while True:
        temp = arr.popleft()
        if temp-i <= 0:
            arr.append(0)
            break
        arr.append(temp-i)
        i+=1
        if i > 5:
            i=1
    print(f'#{tc+1}',*arr)