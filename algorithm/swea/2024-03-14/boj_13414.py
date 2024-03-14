import sys
input = sys.stdin.readline

# k : 학생 수, l : 학생들 총 클릭 수
k,l = map(int,input().split())

dic = {}
basket = []
for i in range(l):
    stu_num = input().rstrip()
    dic[stu_num] = i

dic = dict(sorted(dic.items(), key= lambda x : x[1]))
cnt=0
for i in list(dic.keys())[0:k]:
    print(i)

