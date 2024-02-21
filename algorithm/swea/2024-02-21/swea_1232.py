import sys
sys.stdin = open('1232_input.txt')
sys.stdout = open('1232_output.txt','w')

def sol(start):
    if len(tree[start])>2:
        operator = tree[start][1]  # 연산자
        a = sol(int(tree[start][2])) # 왼쪽
        b = sol(int(tree[start][3])) # 오른쪽
        result=0

        if operator == '+':
            result = a+b
        elif operator == '-':
            result = a-b
        elif operator == '/':
            result = a/b
        elif operator == '*':
            result = a*b
        return result
    else:
        return int(tree[start][1])

for tc in range(10):
   n = int(input())
   tree = [[]]

   for _ in range(n):
       arr = list(input().split())
       tree.append(arr)

   ans = sol(1)
   print(f'#{tc+1} {int(ans)}')
