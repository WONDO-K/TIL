import sys
input = sys.stdin.readline

poket  = {}
n,m = map(int,input().split())
for i in range(n):
    temp = input().rstrip()
    poket[temp] = i+1
    poket[i+1] = temp

for _ in range(m):
    problem = input().rstrip()

    if problem.isdigit():
        print(poket[int(problem)])
    else:
        print(poket[problem])