workers = (
    {1,2,3,7},
    {1,2,3,7},
    {7,},
    {8,3,7},
    {5,2},
)
skills = {2,8,5,7}
numbers = list(map(int, input('Enter the numbers through space: ').split()))
available_skills = set()
for pos, ratings in enumerate(workers):
    for n in numbers:
        if pos == n:
            available_skills.update(ratings)
print(available_skills & skills == skills)