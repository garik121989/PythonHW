def func(n):
  triangles = [[a,b,c] for a in range(1,n+1) for b in range(1,n+1) for c in range(1,n+1) if (a*a + b*b == c*c)]
  return triangles

print(func(6))
