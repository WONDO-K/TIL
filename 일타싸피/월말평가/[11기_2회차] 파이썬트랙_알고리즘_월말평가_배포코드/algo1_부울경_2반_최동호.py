import sys
sys.stdin = open('algo1_sample_in.txt')
sys.stdout = open('algo1_sample_out.txt','w')

def work1(idx,stone_cnt):
    for i in range(stone_cnt):
        if idx+i<=stone:
            arr[idx+i] = arr[idx+i]^1

def work2(idx,stone_cnt):
    color = arr[idx]
    for i in range(1,stone_cnt):
        if idx+i<=stone:
            arr[idx+i] = color


def work3(idx,stone_cnt):
    for i in range(1, stone_cnt+1):
        left_idx = idx - i
        right_idx = idx + i
        if 1 <= left_idx and right_idx <= stone and arr[left_idx] == arr[right_idx]:
            arr[left_idx] ^= 1
            arr[right_idx] ^= 1


for tc in range(int(input())):
    # stone : 돌의 수, cnt : 뒤집기 작업 총 횟수  
    stone,cnt = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.insert(0, 0)

    # x : 기준 위치, y : 작업할 돌의 갯수, w 는 작업 번호
    for _ in range(cnt):
        x,y,w = map(int,input().split())
        if w==1:
            work1(x,y)
        elif w==2:
            work2(x,y)
        elif w==3:
            work3(x,y)
    print(f"#{tc+1} {' '.join(map(str,arr[1:]))}")
