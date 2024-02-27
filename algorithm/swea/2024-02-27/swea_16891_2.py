def check():
    pass

for tc in range(int(input())):
    arr = list(map(int,input().split()))
    temp_1 = [0 for i in range(10)]
    temp_2 = [0 for i in range(10)]
    temp_3 = ''
    result = 0

    for i in range(12):
        if i%2==0:
            temp_1[arr[i]]+=1
            temp_3=temp_1
        elif i%2==1:
            temp_2[arr[i]]+=1
            temp_3 = temp_2

        if check(temp_3):
    print(f'#{tc+1} {result}')