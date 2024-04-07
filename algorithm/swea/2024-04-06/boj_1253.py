import sys
input=sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
num.sort()


cnt=0
for idx,target in enumerate(num):
    temp = num[:idx]+num[idx+1:]

    start, end = 0, len(temp)-1

    while start < end:

        sum_v = temp[start]+temp[end]

        if sum_v == target:
            cnt+=1
            break
        elif sum_v < target:
            start+=1
        else:
            end-=1

print(cnt)