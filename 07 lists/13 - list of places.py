result = [12, 46, 23, 12, 56, 78]
print(result)
rating = [0] * len(result)
place = 1
while place <= len(result):
    for idx, num in enumerate(result):
        if num == max(result) and result.count(num) == 1:
            result[idx] = 0
            rating[idx] = place
            place += 1
        elif num == max(result) and result.count(num) == 2:
            result[idx] = 0
            rating[idx] = place
            place += 1
print(rating)