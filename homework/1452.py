# 아래 함수를 수정하시오.
def remove_duplicates_to_set(arr):
    return set(arr)
    
def remove_duplicates_to_set2(arr):

    number_set = {arr[0]}

    for number in arr[1:]:
        if number not in number_set:
            number_set.add(number)
    return number_set

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
print(remove_duplicates_to_set2([1, 2, 2, 3, 4, 4, 5]))
