import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

N = int(input())
arr = list(map(int,input().split()))

max_v=0

for i in range(N-1) : # for i:0 -> N
    cnt=0 # 오른쪽에 있는 더 낮은 높이의
    for j in range(i+1,N): #for j : i+1->N-1
        if arr[i]>arr[j]:
            cnt+=1
    if max_v < cnt: # 최대 낙차보다 크면
        max_v = cnt
print(max_v)