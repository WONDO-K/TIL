# 0 1 2 3 4 5 4 3 2 1 0

def sol(x):
    if x==6:
        return
    print(x,end=' ')
    sol(x+1)
    print(x,end=' ')

sol(0)