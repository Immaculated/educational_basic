number_of_students_a = int(input('enter number of students in class a\n'))
number_of_students_b = int(input('enter number of students in class b\n'))
number_of_students_c = int(input('enter number of students in class c\n'))
desks_quantity_a = (number_of_students_a + 1) // 2
desks_quantity_b = (number_of_students_b + 1) // 2
desks_quantity_c = (number_of_students_c + 1) // 2
total_desks = desks_quantity_a + desks_quantity_b + desks_quantity_c
print(str(total_desks) + ' total desks needed')