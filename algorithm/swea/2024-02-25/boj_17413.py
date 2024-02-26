import sys
input = sys.stdin.readline

arr = list(input().rstrip())
idx=0
start=0
trans=[]
while idx<len(arr):  # idx가 마지막 인덱스인 len(arr)-1 까지
    if arr[idx]=='<':
        idx+=1
        while arr[idx]!='>':
            idx+=1
        idx+=1 # 마지막 arr[idx]가 '>"이기 때문에 넘겨줘야함
    elif arr[idx].isalnum():
        start = idx
        while idx<len(arr) and arr[idx].isalnum():
            idx+=1
        temp = arr[start:idx]
        temp = temp[::-1]
        arr[start:idx] = temp
    else: #공백 일 때
        idx+=1

print(''.join(arr))
