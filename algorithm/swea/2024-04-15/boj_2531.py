import sys
input = sys.stdin.readline

n,d,k,c = map(int, input().split())

arr = [int(input()) for _ in range(n)]

start,end = 0,1
ans = 0
while start<end and end<=n :
    temp = arr[start:end+1]
    if len(temp) == k:
        # 중복 제거시 길이가 다르면 중복된 초밥이 있다는 의미로 최대한 다양한이라는 조건을 충족 못함
        temp2 = set(temp)
        if len(temp) != len(temp2):
            if ans<len(temp2) and c not in temp2:
                ans = len(temp2)+1
            start+=1
        # 중복이 없을 때
        else:
            if c in temp:
                ans=k

            else:
                ans=k+1
            start += 1
    else:
        end+=1

print(ans)