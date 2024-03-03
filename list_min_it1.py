#Գրեք ծրագիր, որը օգտվողին թույլ կտա մուտքագրել ամբողջ թվային զանգվածի էլեմենտների
#արժեքները և տպում է էկրանին նվազագույնի արժեքը:

def min_list(n:int)->int:
    ls = []
    for i in range(n):
        ls.append(input('please enter number'))
    min = ls[0]
    for i in  range(1,len(ls)):
        if ls[i] < min :
            min = ls[i]
    return min


print(min_list(5))