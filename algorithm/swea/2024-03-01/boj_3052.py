import sys
input = sys.stdin.readline

arr = []
for _ in range(10):
    temp = int(input())
    arr.append(temp%42)

result = set(arr)
print(len(result))