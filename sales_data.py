sales_data=[
{'month':'January','sales':[500,750,321,910,621,410,890,720,331,641,530,780]},
{'month':'February','sales':[420,911,610,371,900,680,431,561,421,711,871,520]},
{'month':'March','sales':[361,490,721,621,311,810,660,780,561,421,471,691]},
{'month':'April','sales':[781,621,431,590,811,641,371,721,881,521,391,671]},
{'month':'May','sales':[930,680,440,571,841,730,311,671,931,561,321,481]},
{'month':'June','sales':[711,481,931,721,511,841,361,731,471,891,651,521]},
{'month':'July','sales':[811,591,341,971,671,431,751,621,411,881,391,761]},
{'month':'August','sales':[940,731,591,421,841,611,371,721,891,561,331,811]},
{'month':'September','sales':[961,721,381,561,821,661,431,791,521,891,471,741]},
{'month':'October','sales':[921,681,341,811,651,421,791,561,331,711,491,761]},
{'month':'November','sales':[951,711,381,671,441,831,621,391,771,531,911,481]},
{'month':'December','sales':[921,781,511]}
]
key = []
value = []
for i in sales_data:
    for j in i.values():
        if isinstance(j,str):
            key.append(j)
        else:
            value.append(sum(j))

#print(key, value)

my_dict = dict(zip(key,value))
print(my_dict)

ls_my_dict =list(my_dict.items())
#print(ls_my_dict)

ls_months = []

for i in range(len(ls_my_dict)):
    res = ls_my_dict[i-1][1]
    if ls_my_dict[i][1] < res:
        ls_months.append(ls_my_dict[i][0])
print(ls_months)


# res = {key:value for key,value in tuple(i.values()) for i in sales_data }


# print(res)