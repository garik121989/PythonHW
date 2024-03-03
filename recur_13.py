#Իրականացնել ռեկուրսիվ ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների
#գումարը:

def func(num:int)->int:

    if num == 0:
        return num
    else:
        return  num % 10 + func(num // 10)


print(func(8))
