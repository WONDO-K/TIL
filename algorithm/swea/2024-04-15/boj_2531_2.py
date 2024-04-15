import sys
input = sys.stdin.readline

n,d,k,c = map(int, input().split())

arr = [int(input()) for _ in range(n)]

start,end = 0,0
ans = 0
while start != n:
    # 0번이라면 0부터 3까지 4개를 보면 된다.
    end = start+k
    temp = set()
    flag = True
    for i in range(start,end):
        i %= n
        temp.add(arr[i])

        if arr[i] == c:
            flag = False

    cnt = len(temp)
    if flag:
        # 쿠폰에 있는 초밥을 추가
        cnt+=1
    ans = max(ans,cnt)
    start+=1

print(ans)