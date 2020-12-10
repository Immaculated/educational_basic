N, R = map(int, input().split())
points = list(map(int, input().split()))

assert len(points)==N, f'Количество точек не равно {N}'

points.sort()
# print(points)
count = 0
recomended_list = []
while len(points):
    i = 0
    while (i < len(points)) and (points[i] - points[0] <= R) :
        recomended_point = points[i]
        i += 1
    recomended_list.append(recomended_point)
            
    points = [
        point for point in points if abs(point - recomended_point) > R
    ]
print(len(recomended_list))