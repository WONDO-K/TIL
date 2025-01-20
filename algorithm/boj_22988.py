import sys

input = sys.stdin.readline

n,x = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

s,e = 0,n-1
half = x//2
cnt=0
remain = 0 # 짜투리
while s <= e: #s와 e가 교차하면 멈춘다.

    if arr[e] == x: # 오른쪽 끝이 최대 용량이라면
        cnt+=1
        e-=1
        continue # 아래 절차 무시하고 다시 시작

    if s==e:
        remain+=1
        break

    if arr[e] + arr[s] >= x/2:
        cnt+=1
        s+=1
        e-=1 
    else: # 절반보다 작을 경우
        s+=1 # 수가 커진다
        remain+=1

print(cnt+remain//3) # 남은 병 3개는 무조건 1개의 가득찬 병이 되기 때문에 3을 나눈다.