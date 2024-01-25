# 아래 함수를 수정하시오.
def difference_sets(dic1,dic2):
    # a에는 있고 b에는 없는 항목으로 세트형 자료구조 생성후 리턴
    # 즉 a-b 
    return dic1.difference(dic2)


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
