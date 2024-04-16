import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque()
for _ in range(n):
    arr.append(input().rstrip())

temp = []
while arr:
    start, end = 0, len(arr)- 1
    a,b = ord(arr[start]), ord(arr[end])
    if a == b and len(arr)>=4:
        c, d = ord(arr[start + 1]), ord(arr[end - 1])
        if c > d:
            temp.append(arr.pop())
        else:
            temp.append(arr.popleft())
    else:
        # 아스키 코드가 더 작은 쪽을 저장한다.
        if a > b:
            temp.append(arr.pop())
        else:
            temp.append(arr.popleft())
cnt=0

for i in temp:
    if cnt % 80 == 0 and cnt != 0:
        print()
    else:
        print(i,end='')
        cnt+=1

