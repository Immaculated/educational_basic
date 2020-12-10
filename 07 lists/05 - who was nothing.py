gen_list = [i for i in range(1,10)]
print('it was starting list: ' + str(gen_list))
max_index = gen_list.index(max(gen_list))
min_index = gen_list.index(min(gen_list))
gen_list[max_index], gen_list[min_index] = gen_list[min_index], gen_list[max_index]
print('list after replacing: ' + str(gen_list))