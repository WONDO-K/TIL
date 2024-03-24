import sys
sys.stdin = open('16663_2_input.txt')

for tc in range(int(input())):
    num = input()

    print(num)
    print(hex(int(num,2))[2:].upper())

    print(int(num,2))
    print(hex((int(num,2))))