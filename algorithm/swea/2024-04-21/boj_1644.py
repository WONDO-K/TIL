import sys
input = sys.stdin.readline

def is_prime(n):

    for i in range(2,int(n**0.5)+1):
        if prime[i]:
            for j in range(2*i,n+1,i):
                prime[j] = False

    for i in range(2,n+1):
        if prime[i]:
            arr.append(i)

n = int(input())
prime = [True]*(n+1)
arr = [0]
is_prime(n)

start,end,ln = 0,0,len(arr)
sum_v=0
cnt=0

while start<ln:
    if sum_v <= n:
        if sum_v == n:
            cnt+=1
        if end<ln-1:
            end+=1
            sum_v+=arr[end]
        else:
            break
    else:
        sum_v-=arr[start]
        start+=1

print(cnt)