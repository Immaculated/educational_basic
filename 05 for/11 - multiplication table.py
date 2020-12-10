for i in range(1, 10):
    for j in range(2, 10): # сделал от 2, потому что не влезало в 80 символов, поэтому съезжало
        print(f'{i} x {j} = {i * j}\t', end= '')
    print('')