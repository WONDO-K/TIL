import sys
sys.stdin = open('1222_input.txt')
sys.stdout = open('1222_output.txt','w')

for tc in range(10):
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 밖에서의 우선순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 안에서의 우선순위
    n = int(input())
    fx = input()
    stack = []
    result = []
    for tk in fx:
        if tk.isdigit():
            result.append(tk)
        else:
            if tk == '(':
                stack.append(tk)
            elif tk in '*/+-':
                if len(stack)==0 or icp[tk] > isp[stack[-1]]:
                    stack.append(tk)
                elif icp[tk] <= isp[stack[-1]]:
                    while isp[stack[-1]] >= icp[tk]:
                        result.append(stack.pop())
                        if len(stack)==0:
                            break
                    stack.append(tk)
            elif tk == ')':
                while stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop
    result.append(stack.pop())
    print(f'result : {result}')
    print(f'stack : {stack}')
    while result:
        if result[0].isdigit():
            stack.append(result.pop(0))
        elif result[0] in '*/+-':
            a,b = stack.pop(),stack.pop()
            if result.pop(0) == '+':
               stack.append(int(a)+int(b))
    print(f'#{tc+1}', *stack)




