import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    arr = list(input())
    stack = []

    for i in arr:
        if i == '{' or i == '(':
            stack.append(i)
        elif  i == '}':
            # stack이 비어있는 경우는 바로 false로 처리되어 pop을 실행하지 않는다.
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
        elif i== ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')
