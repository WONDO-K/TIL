import sys
sys.stdin = open('minc_07_input.txt')
sys.stdout = open('minc_07_output.txt', 'w')

for tc in range(int(input())):
    s1_x1,s1_y1,s1_x2,s1_y2 = map(int,input().split())
    s2_x1,s2_y1,s2_x2,s2_y2 = map(int,input().split())
    ans=0
    if (s2_x1<s1_x1<s2_x2 and s2_y1<s1_y2<s2_y2) or (s1_x1<s2_x1<s1_x2 and s1_y1<s2_y1<s1_y2):
        ans = 1
    elif s1_x2==s2_x1 or s1_y2==s2_y1 or s1_x1==s2_x2 or s1_y1==s2_y2:
        if (s1_x1,s1_y1)==(s2_x2,s2_y2) or (s1_x2,s1_y2)==(s2_x1,s2_y1) or (s1_x1,s1_y1)==(s2_x1,s2_y1) or (s1_x2,s1_y2)==(s2_x2,s2_y2):
            ans=3
        else:
            ans = 2
    else:
        ans=4
    print(f'#{tc+1} {ans}')