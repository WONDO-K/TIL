import sys
from collections import deque
sys.stdin = open('4408_input.txt')
sys.stdout = open('4408_output.txt','w')

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    number = []

    for i in arr:
        i.sort()
        number.extend(i)

    stack = []
    cnt = 1

    for num in number:
        if not stack or stack[-1]<num:
            stack.append(num)
            print(f' len(stack)==0 or stack[-1]<num, stack : {stack}')
        else:
            while stack and stack[-1] >= num:
                stack.pop()  # 스택의 최상단이 현재 숫자보다 클 때까지 pop
            stack.append(num)  # 현재 숫자를 스택에 추가
            cnt += 1  # 간선의 개수 증가
            print(f'pop cnt : {cnt}')

    # while number:
    #     num = number.pop(0)
    #     print(f'num : {num} ')
    #     if not stack or stack[-1]<num:
    #         stack.append(num)
    #         print(f' len(stack)==0 or stack[-1]<num, stack : {stack}')
    #     else:
    #         while stack and stack[-1]<num:
    #             stack.pop()
    #             print(f'after pop stack : {stack}')
    #             cnt+=1
    #             stack.append(num)
    #             print(f'stack : {stack}')

    print(f'#{tc+1} {cnt}')