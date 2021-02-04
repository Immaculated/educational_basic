def additor(number = 0, filename='additor.data'):
    try: 
        with open(filename,'x') as file:
            file.write('0')
    except FileExistsError:
        with open(filename, 'r') as file:
            prev = file.read().split('\n')        
        with open(filename, 'a') as file:
            file.write('\n' + str(int(prev[-1]) + number))
additor(100)
additor(1000)
additor(111111)
!more additor.data