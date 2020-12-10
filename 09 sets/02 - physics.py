set_math = {'Simpson', 'Griffin', 'Fry', 'Rodriguez', 'Farnsworth'}
set_phys = {'Zoidberg', 'Wong', 'Wernstrom', 'Scruffy', 'Farnsworth'}
both = set_math.union(set_phys)
only_math = set_math.difference(set_phys)
only_phys = set_phys.difference(set_math)
print(' math + phys: ' , str(both) , '\n' , 'only math: ' , str(only_math), '\n' , 'only phys: ' ,  str(only_phys))