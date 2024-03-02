import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())

cnt = [ 0 for i in range(n+1)]
cnt[1]=1
idx=1
move=0
while True:
    if cnt[idx]==m:
        break
    else:
        if cnt[idx]%2==0: # 짝 수일 때
            idx-=l
            if idx<1:
                idx+=n
            cnt[idx] += 1
            move+=1
        else: # 홀 수 일때
            idx+=l
            if idx>n:
                idx-=n
            cnt[idx] += 1
            move+=1

print(move)