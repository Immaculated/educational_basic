n = int(input("enter quantity of white balls\n"))
m = int(input("enter quantity of black balls\n"))
pa = float(n / (m + n)) # вероятность того,что первый шар белый
pb = float((n - 1) / (m + n - 1)) # вероятность того, что второй шар тоже белый
pab = float(pa * pb) # вероятность того, что оба вынутых шара белые
print("вероятность того, что оба шара белые = " + str(pab))