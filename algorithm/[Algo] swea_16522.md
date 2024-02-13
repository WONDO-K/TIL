```python

for tc in range(int(input())):
    arr = input().split()
    stack = []
    while arr:
        if arr[0] == '.':
            if len(stack)!=1:
                result = 'error'
                break
            result = stack.pop()
            break
        else:
            if arr[0].isdigit():
                stack.append(arr.pop(0))

            elif arr[0] in '*/+-':
                if len(stack) < 2:  # stack에 있는 top,top-1의 값을 pop할 때 원소의 개수가 2개 이하라면 연산자와 피연산자의 짝이 안맞음
                    result = 'error'
                    break
                else:  # stack에 2개 이상의 값이 있기 때문에 아직 연산자와 피연산자의 짝이 맞는 중
                    b, a = stack.pop(), stack.pop()
                    operator = arr.pop(0)
                    if operator == '+':
                        stack.append(int(a) + int(b))
                    elif operator == '-':
                        stack.append(int(a) - int(b))
                    elif operator == '*':
                        stack.append(int(a) * int(b))
                    elif operator == '/':
                        stack.append(int(a) // int(b))
    print(f'#{tc + 1} {result}')


```