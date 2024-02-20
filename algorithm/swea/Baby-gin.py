import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())

for tc in range(1, T + 1):

    fake_arr = input()
    arr=[]
    for i in range(6):
        arr.append(int(fake_arr[i])%10)

    cnt = [0 for _ in range(10)]

    for i in arr:
        cnt[int(i)]+=1

    letter = 6

    for i in range(len(arr)):
        idx = arr[i]
        if cnt[idx] >= 3:
            letter -= (3*(cnt[idx] // 3 ))
            cnt[idx] = cnt[idx] % 3

        if cnt[idx] == 2 and idx != (len(cnt)-1) :
            if cnt[idx+1] == 2 and cnt[idx+2]==2:
                cnt[idx+1]-=2
                cnt[idx+2]-=2
                letter -= 6

        if cnt[idx]>=1 and idx != (len(cnt)-1):
            if cnt[idx+1]>=1 and cnt[idx+2]>=1:
                cnt[idx]-=1
                cnt[idx+1]-=1
                cnt[idx+2]-=1
                letter-=3
    if letter == 0:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')