import math
a, b, h = map(int, input('enter start, stop, step\n').split())
print('fuction values in line segment:')
print(f'x | fx')
for x in range(a, b + 1, h):
    f = math.pow(x, 2) - math.sin(x)
    fx = round(f, 2)
    print(x, str(fx), sep = ' | ')