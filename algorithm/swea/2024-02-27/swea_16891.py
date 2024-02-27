def triplet_check(arr):
    cnt = [0 for i in range(10)]
    for num in arr:
        cnt[num]+=1

    if 3 in cnt:
        return True
    return False

def run_check(arr):
    arr.sort()
    cnt=1
    for i in range(len(arr)-1):
        if arr[i]+1 == arr[i+1]:
            cnt+=1
        else:
            cnt=1
    if cnt==3:
        return True
    return False

for tc in range(int(input())):
    arr = list(map(int,input().split()))
    temp_1,temp_2=[],[]

    # 0 : run, 1: triplet
    check1=[False,False]
    check2=[False,False]
    result=0
    for i in range(len(arr)):
        if i%2==0:
            temp_1.append(arr[i])
            if len(temp_1)>=3:
                check1[0] = run_check(temp_1)
                check1[1] = triplet_check(temp_1)
                if check1[0] or check1[1] == True:
                    result=1
                    break
        else:
            temp_2.append(arr[i])
            if len(temp_2) >= 3:
                check2[0] = run_check(temp_2)
                check2[1] = triplet_check(temp_2)
                if check2[0] or check2[1] == True:
                    result=2
                    break
    # print(f'check1 : {check1}')
    # print(f'check2 : {check2}')
    print(f'#{tc+1} {result}')