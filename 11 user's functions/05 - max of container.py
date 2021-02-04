def max_two(a,b):
    return a if a > b else b

def max_container(cont):
    elem = 0
    for x in cont:
        maximal = max_two(x, elem)
        elem = maximal
    return maximal
print(max_container([3, 33, 3333, 33333]))