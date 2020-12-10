i = 0
a, b, c = 3, 4, 5
for a in range(3, 100):
    for b in range(4, 100):
        c = (a ** 2 + b ** 2) ** (1/2)
        for c in range(5, 100):
            if a < b < c and (a ** 2 + b ** 2 == c ** 2) : 
                i += 1
print('quantity of triangles = ' + str(i))