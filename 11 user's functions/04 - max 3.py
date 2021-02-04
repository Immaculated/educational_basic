def max_two(a,b):
    return a if a > b else b

def max_three (a, b, c):
    return max_two(max_two(a,b), max_two(b,c))
print(max_three(1, 2, 3))