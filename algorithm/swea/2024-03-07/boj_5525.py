import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

# Pn은 무조건 I부터 시작한다. index()를 통해 가장 먼저 등장하는 I의 위치부터 시작
start = s.index('I')
limit = (n+1)+n

pn = ''

for i in range(limit):
    if i%2==0:
        pn+='I'
    else:
        pn+='O'

cnt=0
for i in range(start,m-limit+1):
    if s[i:i+limit] == pn:
        cnt+=1

print(cnt)