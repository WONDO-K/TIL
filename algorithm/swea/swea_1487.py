import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

T = int(input())
N,W = map(int,input().split(','))
arr = list(map(int,input().split()))
arr.sort()

