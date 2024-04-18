import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

temp = ''
start = 0
end = n-1
while start<=end:
    left,right = arr[start],arr[end]
    if left<right:
        temp += left
        start += 1
    elif left>right:
        temp += right
        end -= 1
    else: # 만약 같다면 마지막 하나 남았으니 추가하고 종료
        if end-start<=1:
            temp += left
            start+=1
        else:
            start2 = start+1
            end2 = end-1

            while start2<=end2:
                left2, right2 = arr[start2], arr[end2]
                if left2<right2:
                    temp += left
                    start+=1
                    break
                elif left2>right2:
                    temp += right
                    end-=1
                    break
                elif end2-start2<=1:
                    temp += left
                    start+=1
                    break
                else: # start2와 end2가 서로 같다면
                    start2+=1
                    end2-=1
cnt=0

for i in temp:
    if cnt != 0 and cnt % 80 == 0:
        print()
    else:
        print(i,end='')
        cnt+=1

