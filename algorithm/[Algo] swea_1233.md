# [Algo] 2024-02-13
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

```python
for tc in range(10):
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 밖에서의 우선순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 안에서의 우선순위
    n = int(input())
    fx = input()
    stack = []
    result = []

    for tk in fx:
        if tk == '(':
            stack.append(tk)
        elif tk in '*/+-':
            if len(stack) == 0 or icp[tk] > isp[stack[-1]]:
                stack.append(tk)
            elif icp[tk] <= isp[stack[-1]]:
                while stack and isp[stack[-1]] >= icp[tk]:
                    result.append(stack.pop())
                stack.append(tk)
        elif tk == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            result.append(tk)
    # 남은 연산자 stack에 삽입
    while stack:
        result.append(stack.pop())
        
    for tk in result:
        if tk.isdigit():
            stack.append(tk)
        else:
            b, a = stack.pop(), stack.pop()
            if tk == '*':
                stack.append(int(a)*int(b))
            else:
                stack.append(int(a)+int(b))

    print(f'#{tc + 1}', *stack)
```

- 연산자가 계속 남아있는 문제가 있었는데 이를 남김없이 result에 삽입하여 줌으로써 해결함