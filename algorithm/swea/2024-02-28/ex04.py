# time = [15,30,50,10]
# n = len(time)
# time.sort()
#
# result=[0]*n
#
# for i in range(1,n):
#     result[i] = result[i-1]+time[i]
#
# print(sum(result))
person = [15,30,50,10]
n = len(person)
person.sort()
sum = 0
left_person = n-1

for turn in range(n):
    time = person[turn]
    sum+=left_person*time
    left_person-=1
print(sum)