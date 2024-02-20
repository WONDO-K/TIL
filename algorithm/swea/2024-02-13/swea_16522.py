import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    arr = list(input().split())
    print(f'arr : {arr}')
    stack = []
    # while result:
    #     if result[0].isdigit():
    #         stack.append(result.pop(0))
    #     elif result[0] in '*/+-':
    #         a,b = stack.pop(),stack.pop()
    #         if result.pop(0) == '+':
    #            stack.append(int(a)+int(b))

    # while arr:
    #     if arr[0].isdigit():
    #         stack.append(arr.pop(0))
    #     elif arr[0] in '*/+-':
    #         a,b = stack.pop(), stack.pop()
    #         print(f'a:{a}, b:{b}')
    #         if arr[0] == '+':
    #             arr.pop(0)
    #             stack.append(int(a) + int(b))
    #         elif arr[0] == '-':
    #             arr.pop(0)
    #             stack.append(int(a) - int(b))
    #         elif arr[0] == '*':
    #             arr.pop(0)
    #             stack.append(int(a) * int(b))
    #         elif arr[0] == '/':
    #             arr.pop(0)
    #             stack.append(int(a) / int(b))
    flag=True
    while arr:
        print(f'arr : {arr}')
        if arr[0] == '.':
            break
        else:
            if arr[0].isdigit():
                stack.append(arr.pop(0))
                print(f'stack : {stack}')

            elif arr[0] in '*/+-':
                print(f'arr[0] : {arr[0]}')
                if len(stack)<=1:
                    break
                else:
                    if len(arr)<2:
                        break
                    else:
                        b, a = stack.pop(), stack.pop()
                        print(f'a:{a}, b:{b}')
                        operator = arr.pop(0)
                        print(f'operator : {operator}')
                        if operator == '+':
                            stack.append(int(a) + int(b))
                        elif operator == '-':
                            stack.append(int(a) - int(b))
                        elif operator == '*':
                            stack.append(int(a) * int(b))
                        elif operator == '/':
                            stack.append(int(a)/int(b))
                        print(f'after stack : {stack}')
    print()
if len(arr)==1 and arr[0]=='.':
    print(f'#{tc+1}', stack)
else:
    print(f'#{tc+1} error')