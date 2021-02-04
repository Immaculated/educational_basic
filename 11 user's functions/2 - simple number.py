def simple_number(n):
    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0 and n != i:
                print('number is composite')
                break
        else: print('number is simple')
    else:
        print('number is one, zero or negative')
simple_number(11)
simple_number(12)
simple_number(1)
simple_number(0)
simple_number(-10)