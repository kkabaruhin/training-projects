x = [[1, 2, 3], [4, 5, 6], [7,8,9]]
y = x.copy()
x[0][0] = 11

print(y)
print(x)