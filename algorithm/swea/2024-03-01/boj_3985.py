import sys
input = sys.stdin.readline
from collections import deque


l = int(input())
n = int(input())

customer = deque()
for _ in range(n):
    start,end = map(int,input().split())
    customer.append([start,end])

# 방문 체크
visit = [0]*(l+1)

person_num = 1
# 차이 측정
dist = -float('inf')
max_cnt = -float('inf')
person1 = 0
person2 = 0

for _ in range(n):
    start,end = customer.popleft()
    num_cnt=0
    if dist<end-start:
        dist = end-start
        person1 = person_num
    for i in range(start,end+1):
        if visit[i]==0:
            visit[i] = 1
            num_cnt+=1
        if max_cnt<num_cnt:
            max_cnt = num_cnt
            person2 = person_num
    person_num+=1

print(person1)
print(person2)