import sys
sys.stdin = open('18907_input.txt')
sys.stdout = open('18907_output.txt', 'w')

def quick(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    p_arr = arr[1:]

    left_arr = [x for x in p_arr if  x<=pivot] # pivot보다 작거나 같은 경우
    right_arr = [x for x in p_arr if x>pivot] # pivot보다 큰 경우

    return quick(left_arr) + [pivot] + quick(right_arr)

for tc in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    arr = quick(num)
    print(f'#{tc+1} {arr[n//2]}')
