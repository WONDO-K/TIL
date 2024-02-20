import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for tc in range(int(input())):
    cnt = [0 for i in range(10)]

    N = int(input())
    arr = list(input())

    for i in arr:
        cnt[int(i)]+=1
    max_idx = 0

    for i in range(1,len(cnt)):
        if cnt[i] >= cnt[max_idx]:
            max_idx = i
    print(f'#{tc+1} {max_idx} {cnt[max_idx]}')