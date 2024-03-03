#Գրեք ծրագիր, որը օգտվողին թույլ կտա մուտքագրել ամբողջ թվային զանգվածի էլեմենտների
#արժեքները և տպում է նվազագույն և առավելագույն արժեքներով էլեմենտների գումարը:

def min_max(n:int)->int:
    ls = []

    for i in range(n):
        ls.append(int(input('please neter number')))
    mi_n = ls[0]
    m_ax = ls[0]
    for i in range(1,len(ls)):
        if ls[i] < mi_n:
            mi_n = ls[i]

        if ls[i] > m_ax:
            m_ax = ls[i]
    return(mi_n + m_ax)


print((min_max(5)))





