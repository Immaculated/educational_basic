def mse(list_1, list_2):
    if len(list_1) != len(list_2):
        raise Exception("Lens of lists are not equal")
    else:
        return sum([(x - y) ** 2 for x, y in zip(list_1, list_2)]) / len(list_1)
print(mse([11, 12, 14, 12], [13, 13, 12, 11]))
print(mse([11, 12, 14, 12], [13]))