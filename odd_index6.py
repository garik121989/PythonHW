#Իրականացնելֆունկցիա, որըկստանա list և կվերադարձնի նոր list, որը պարունակում է սկզբնական list - ի կենտ ինդեքսներում եղած արժեքները:


def odd_index(ls:list)->list:
    new_ls = [ls[i] for i in range(len(ls)) if i % 2 != 0]
    #new_ls = []
    # for i in range(len(ls)):
    #     if i % 2 != 0:
    #         new_ls.append(ls[i])
    return new_ls

print(odd_index([22,2,3,28,5,6,7,72,143]))