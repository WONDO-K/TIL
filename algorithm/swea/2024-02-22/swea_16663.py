import sys
sys.stdin = open('16663_input.txt')
sys.stdout = open('16663_output.txt', 'w')

for tc in range(int(input())):
    n,arr = input().split()
    arr =list(arr)
    for i in range(len(arr)):
        if arr[i].isdigit():
            arr[i] = bin(int(arr[i]))[2:].zfill(4)
        else:
            arr[i] = bin(int(arr[i],16))[2:].zfill(4)
    print(f'#{tc+1} ',end='')
    for i in arr:
        print(i,end='')
    print()
#
# for tc in range(int(input())):
#     data = input().split()
#     numbers = data[1]
#
#     binary_result = ''
#     for digit in numbers:
#         if digit.isdigit():
#             binary_result += bin(int(digit))[2:].zfill(4)
#         else:
#             binary_result += bin(int(digit, 16))[2:].zfill(4)
#
#     print(f'#{tc + 1} {binary_result}')