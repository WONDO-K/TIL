import sys
sys.stdin = open('4366_input.txt')
sys.stdout = open('4366_output.txt', 'w')

def solve(a,b):
    for i in range(len(a)):
        temp1 = a.copy()
        temp1[i] = str(int(temp1[i])^1)
        # print(f'temp1:{temp1}')
        for j in range(len(b)):
            temp2 = b.copy()
            for k in range(3):# 3진수는 0,1,2 숫자 3개만 사용한다.
                temp2[j] = str(k)
                # print(f'temp2:{temp2}')
                a_dec = int(''.join(temp1), 2)
                b_dec = int(''.join(temp2), 3)
                # print(f'a_dec:{a_dec}')
                # print(f'b_dec:{b_dec}')
                if a_dec == b_dec:
                    return a_dec

for tc in range(int(input())):
    a = list(input())
    b = list(input())

    print(f'#{tc+1} {solve(a,b)}')