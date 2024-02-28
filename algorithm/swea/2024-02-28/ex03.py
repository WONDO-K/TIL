# 중복순열
n = 3
path = []

def func(lev):
    if lev == n:
        print(path)
        return

    for i in range(1,7): # 브랜치는 6
        path.append(i)
        func(lev+1)
        path.pop()
func(0)