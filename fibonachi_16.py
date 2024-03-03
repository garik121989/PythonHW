#Գրել ֆունկցիա, որը որպես պարամետր կստանա n թիվը և կվերադարձնի n-րդ Ֆիբոնաչիի թիվը:

def func(n):
    ls = [0]
    item = n
    if n <= 1:
        return n
    else:
      return func(n-1) + func(n-2)


print(func(10))
