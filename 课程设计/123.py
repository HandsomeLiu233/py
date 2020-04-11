'''

# 凯撒加密
import string

def kaisa(strr,num):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    before=lower+upper
    after=lower[num:]+lower[:num]+upper[num:]+upper[:num]
    table=str.maketrans(before,after)
    return strr.translate(table)

print(kaisa('i love py',26))
'''
'''
with open('score.txt',encoding='utf-8') as fp:
    for line in fp:
        print(line)
'''

import string

a='Hello world!'[-4:]
print(a)
