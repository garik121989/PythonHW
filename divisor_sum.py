def func(n):
    res = sum([a for a in range(1, n + 1) if n % a == 0])
    return res

print(func(8))
