# 중복순열
n = 3
path = []

def func(lev,start):
    if lev == n:
        print(path)
        return

    for i in range(start,7): # 브랜치는 6
        path.append(i)
        func(lev+1,i)
        path.pop()

func(0,1)