import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

temp = []
start, end = 0, n - 1
while start <= end:
    left, right = arr[start], arr[end]
    if left < right:
        temp.append(left)
        start += 1
    elif left > right:
        temp.append(right)
        end -= 1
    else:  # 만약 같다면
        temp.append(left)  # 중복 요소 추가
        # 중복된 요소 건너뛰기
        while start < end and arr[start] == left:
            start += 1
        while start < end and arr[end] == right:
            end -= 1

# 출력
cnt = 0
for i in temp:
    if cnt % 80 == 0 and cnt != 0:
        print()
    print(i, end='')
    cnt += 1
