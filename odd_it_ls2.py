#Գրել ծրագիր, որը կտպի զանգվածի կենտ էլեմենտների քանակը
def func(ls:list)->int:
    res = 0
    for i in ls:
        if i % 2 != 0:
            res += 1
    return res

print(func([1,2,3,4,5,6,7,8,9,11]))