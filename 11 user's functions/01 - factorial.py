def fctrl(n):
    if n == 0:
        return 1
    else:
        return fctrl(n-1) * n
print(fctrl(10))