def replacing(starting_dict):
    temporary_dict = {}
    for key, value in starting_dict.items():
        temporary_dict[value] = key
    starting_dict = temporary_dict
    return starting_dict
def rtest(first_dict, second_dict):
    return first_dict == replacing(second_dict)
print('original dict ' + str({'Leo': 11, 'Raph': 12, 'Mickey': 13, 'Don': 14}))
print('replaced dict ' + str(replacing({'Leo': 11, 'Raph': 12, 'Mickey': 13, 'Don': 14})))
print('test: ' + str(rtest({'Leo': 11, 'Raph': 12, 'Mickey': 13, 'Don': 14}, {11: 'Leo', 12: 'Raph', 13: 'Mickey', 14: 'Don'})))