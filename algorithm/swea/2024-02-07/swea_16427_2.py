import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    arr = list(input())
    stack=[arr[0]]
    for i in arr[1:]:
        if i!=stack[-1]:
            stack.append(i)
        elif i==stack[-1]:
            stack.pop()
    print(f'#{tc+1} {len(stack)}')
