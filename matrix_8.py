#Ստեղծել NxN չափի մատրից և տպել մատրիցի առաջին և երրորդ սյուները: N >=4: (Slicing)

matrix = [[i, i +1, i + 2, i + 3] for i in range(1,16,4)]
print((matrix))

for row in matrix:
    print(row[::2])