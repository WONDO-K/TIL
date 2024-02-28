import sys
sys.stdin = open('16918_input.txt')
sys.stdout = open('16918_output.txt','w')



for tc in range(int(input())):
    n = int(input())
    time_table = []
    for i in range(n):
        time_table.append(list(map(int,input().split())))

    time_table.sort(key=lambda x : (x[1],x[0]))
    start,end = time_table[0][0],time_table[0][1]
    cnt=1
    for i in range(1,n):
        next_s, next_e = time_table[i][0], time_table[i][1]
        if next_s>=end:
            end = next_e
            cnt+=1
    print(f'#{tc+1} {cnt}')