def func(num:int):
    tmp = 0
    count = 0
    if str(num) == str(num)[::-1]:
        print('number is polindrom')
        return 0
    else:
        while True:
            count += 1
            pol =  num + int(str(num)[::-1])
            if str(pol) == str(pol)[::-1]:
                return pol,count
            num = pol
print(func(1249))