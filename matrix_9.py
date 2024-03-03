#Ստեղծել NxN չափի մատրից և տպել առաջին և չորրորդ տողերի մաքսիմալ և մինիմալ
#էլեմենտների գումարը: N >= 4:

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
res = 0
# min  = 0
# max = 0
for i in range(0,len(matrix),3):
    #     res = res + min(matrix[i]) + max(matrix[i])
        for j in range(1,len(matrix[0])):
            min = matrix[i][0]
            max = matrix[i][0]

            if matrix[i][j] < min:
                min = matrix[i][j]

            if matrix[i][j] > max:
                max = matrix[i][j]
        res = res + min + max

#res = res + min + max
print(res)
