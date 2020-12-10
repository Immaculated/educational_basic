from math import ceil
k = int(input("enter the number of bottles in one bag\n"))
n = int(input("enter the number of bottles total\n"))
num_of_bags_needed = ceil(n / k)
print("u need " + str(num_of_bags_needed) + " bags for ur bottles")