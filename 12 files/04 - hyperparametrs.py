import pickle


def mult_val(param):
    result_lst = []
    for k1, v1 in param_for_search.items():
        for k2, v2 in param_for_search.items():
            if k1 != k2:
                for vl1 in v1:
                    for vl2 in v2:
                        temp_dict = {}
                        temp_dict[k1], temp_dict[k2] = vl1, vl2
                        result_lst.append(tuple([(temp_dict), (vl1 * vl2)]))
        break        
    return result_lst

def gip_file(param, fname='gipper.data'):
    with open(fname, "wb") as file:
        pickle.dump(mult_val(param), file)

def bin_file_print(fname='fib.data'):
    with open(fname, "rb") as file:
        results = pickle.load(file)
        print(results)



param_for_search = {
"learning_rate": [0.01, 0.05, 0.1],
"max_depth": [5,10,15],
}


gip_file(param_for_search)
bin_file_print('gipper.data')