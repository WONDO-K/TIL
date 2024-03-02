import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())

cnt = [ 0 for i in range(n+1)]

print(cnt)
cnt[1]=1
idx=1
move=0
while True:
    print(f'first idx : {idx}')
    print(f'cnt : {cnt}')
    if cnt[idx]==m:
        print(f'move:{move}')
        break
    else: 
        if cnt[idx]%2==0: # 짝 수일 때
            idx-=l
            if idx<1:
                idx+=n
            print(f'if idx:{idx}')
            cnt[idx] += 1
            move+=1
            print('if move')
        else: # 홀 수 일때
            idx+=l
            if idx>n:
                idx-=n
            print(f'else idx:{idx}')
            cnt[idx] += 1
            move+=1
            print('else move')

print(move)