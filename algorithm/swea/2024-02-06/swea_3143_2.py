import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    A, B = input().split()
    print(f'#{tc + 1} {len(A)-len(B)*A.count(B) + A.count(B)}')
