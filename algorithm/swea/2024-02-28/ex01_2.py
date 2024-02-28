arr = ['A','B','C']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1: # 1 비트가 1인지 확인
            print(arr[i],end='')
        tar>>=1

for tar in range(1<<n):
    print('{',end='')
    get_sub(tar)
    print('}')