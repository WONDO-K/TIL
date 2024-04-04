import sys
input=sys.stdin.readline

N = int(input())
count=0
row = [0] * (N+1)

def check(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def queen(x):
    global count
    if x==N:
        count+=1
        return
    else:
        for i in range(N):
            row[x]=i
            if check(x):
                queen(x+1)

queen(0)
print(count)