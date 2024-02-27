def kfc(x):
    if x==3:
        return
    kfc(x+1)
    print(x)

for i in range(2):
    kfc(0)