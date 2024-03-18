import sys
sys.stdin = open('1952_input.txt')
sys.stdout = open('1952_output.txt', 'w')


def sol(cost,plan):
    total = 0
    for month in plan:
        if month <= 4:
            total += month*10




    return total
for tc in range(int(input())):
    costs = list(map(int,input().split()))
    plan = list(map(int,input().split()))

    money = float('INF')

    for cost in costs:
        money = min(money,sol(cost,plan))