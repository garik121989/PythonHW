#Իրականացնել pop ֆունկցիան:
def func_pop(ls:list, in_dex:int)->int:
    if in_dex == None:
        num = ls[-1]
        ls = ls[0:-1]
        print(ls)
        return(num)
    else:
        num = ls[in_dex]
        ls = ls[0:in_dex] + ls[in_dex+1:]
        print(ls)
        return num



print(func_pop([7,2,3,4,89],3))