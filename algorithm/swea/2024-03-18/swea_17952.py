import sys
sys.stdin = open('17952_input.txt')
sys.stdout = open('17952_output.txt', 'w')

def merge_sort(arr):
    global cnt
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    if low_arr[-1]>high_arr[-1]:
        cnt+=1

    merged_arr = []

    l=h=0

    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

for tc in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    cnt=0
    merge_sort(num)
    num.sort()
    print(f'#{tc+1} {num[n//2]} {cnt}')
