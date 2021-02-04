import pickle
def fibonacci(number, a = 0, b = 1):
    fibonacci_list = []
    for temp in range(number):
        fib = a + b
        b, a = a, fib
        fibonacci_list.append(b)
    return fibonacci_list

def fibonacci_file(number, filename='fib.data'):
    with open(filename, "wb") as file:
        pickle.dump(fibonacci(number), file)
    with open(filename, "rb") as file:
        fibbonacci_file_list = pickle.load(file)
        fibbonacci_file_list += (fibonacci(number * 2)[number:]) 
    with open(filename, "wb") as file:
        pickle.dump(fibbonacci_file_list, file)
        
def binary_file_print(filename='fib.data'):
    with open(filename, "rb") as file:
        results = pickle.load(file)
        print(results)
          
fibonacci_file(10)
binary_file_print()