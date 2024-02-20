import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())
for tc in range(1, T + 1):
    s = input()
    # print(s)

    lst = []
    sym = ['(', '{']
    ans = '1'
    for i in s:
        if i in sym:
            lst.append(i)
        
        # lst가 비어있을 경우
        # 현재 검사해야하는 i가 ) 혹은 } 일 경우 바로 정답을 0으로 처리해버림
        # 왜? 어차피 뒤를 확인하지 않아도 짝이 안맞음을 알 수 있다
        if len(lst) == 0:
            if i == ')' or i == '}':
                ans = '0'

        # 스택의 길이가 1이상일 경우
        if len(lst) >= 1:
            # 현재 검사해야하는 i가 )일 경우
            if i == ')':
                # 스택의 top이 '('로 짝이 맞으면 top 삭제
                if lst[-1] == '(':
                    lst.pop()
                # 만약 스택의 top이 '{'이라면 짝이 안맞으므로 정답 바로 0처리
                elif lst[-1] == '{':
                    ans = '0'
            # 현재 검사해야하는 i가 }일 경우
            if i == '}':
                # 스택의 top이 '{' 로 짝이 맞으면 top 삭제
                if lst[-1] == '{':
                    lst.pop()
                # 스택의 top이 '(' 이라면 짝이 안맞으므로 정답 바로 0처리
                elif lst[-1] == '(':
                    ans = '0'

    # 만약 스택에 값이 남았다면 짝이 안맞는다는 의미이므로 정답 0처리
    if len(lst) != 0:
        ans = '0'

    print(f'#{tc} {ans}')