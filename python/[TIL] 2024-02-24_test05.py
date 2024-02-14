a = -16
bin_num=''
if a<0:
    print(f'a : {a}')
    a = abs(a)
    bin_num+='1'
    print(bin_num)
    while a!=1:
        a = a//2
        print(a)
        print(f'bin_num : {bin_num}')
        bin_num+=str(a%2)
        if a==1:
            bin_num+='1'
else:
    print(f'a : {a}')
    bin_num+='0'
    print(bin_num)
    while a!=1:
        a = a//2
        print(a)
        print(f'bin_num : {bin_num}')
        bin_num+=str(a%2)
        if a==1:
            bin_num+='1'

result = sorted(bin_num[1:],reverse=True)


