# for 문으로 구현

arr = ['A','B','C','D','E']
path = []
n=3

for a in range(5):
    start1 = a+1
    for b in range(start1,5):
        start2 = b+1
        for c in range(start2,5):
            print(arr[a],arr[b],arr[c])