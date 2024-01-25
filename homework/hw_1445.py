# 아래 함수를 수정하시오.
def count_character(arr,target):
    return arr.count(target)

def count_character2(arr,target):
    cnt = 0

    for i in arr:
        if i == target:
            cnt+=1
    return cnt

result = count_character("Hello, World!", "o")
result2 = count_character2("Hello, World!", "o")
print(result)  # 2
print(result2) 
