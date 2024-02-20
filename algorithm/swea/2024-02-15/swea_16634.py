import sys
sys.stdin = open('16634_input.txt')
sys.stdout = open('16634_output.txt','w')

for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
   # print(arr)
    i=0
    cnt=0
    while cnt!=m:
        if i==len(arr):
            i=0
        else:
            #print(f'i:{i}, arr[{i}]:{arr[i] // 2}')
            arr[i] //= 2
            #print(arr)
            if arr[i]==0:
                ans = i
                cnt+=1
                # print(f'ans : {ans}')
                # print(arr)
        i+=1
    print(f'#{tc+1} {ans+1}')