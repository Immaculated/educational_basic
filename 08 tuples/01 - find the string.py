my_tupl = (
    'asd ad',
    'name',
    'sy ds da',
    'name',
    'name'
)
find = 'name'

for i in range(len(my_tupl)):
    if find == my_tupl[i]:
        print(i)

for i, elem in enumerate(my_tupl):
    if find == elem:
        print(i)

i = 0
while find in my_tupl[i:]:
    print(my_tupl.index(find, i))
    i = my_tupl.index(find, i) + 1
print('count:', my_tupl.count(find))