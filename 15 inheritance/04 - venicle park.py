import random

# parent class
class Cars():
    colors = ["red","blue","black","white"]
    complete_set=["budget","average","full"]

# heirs of the parent class
class Passenger_cars(Cars):
    number_of_passenger_seats = 5

# heirs of the parent class    
class Trucks(Cars):
    weight = 1500
    maximum_cargo_dimensions = 1500*4000*1700


mylist_passenger=[]#Our list for append generate objects Passenger cars
mylist_weight=[]#Our list for append generate objects Trucks cars

# In this function, we generate the number of objects Passenger_cars and append to our list
def generating_a_random_number_of_passenger_cars():
    for i in range(random.randint(0, 20)):
        mylist_passenger.append(Passenger_cars())
    print(len(mylist_passenger))

# In this function, we generate the number of objects Tricks and append to our list
def generating_a_random_number_of_trucks_cars():
    for i in range(random.randint(0, 20)):
        mylist_weight.append(Trucks())
    print(len(mylist_weight))

# A function that accepts a list of objects Passenger_cars and reads their properties: number_of_passenger_seats
def sum_passendger(List_passenger):
    pass_count = 0
    for elem in List_passenger:
        pass_count += elem.number_of_passenger_seats
    return(pass_count)

# A function that accepts a list of objects Trucks and reads their properties: weight
def sum_weight(List_trucks):
    weight_count = 0
    for elem in List_trucks:
        weight_count += elem.weight
    return(weight_count)

# A function that checks the conditions for comparing the required user-entered data and our calculated class properties
def answer():
        required_number_of_passenger_seats = int(input("Enter required number of passenger seats:  "))
        required_number_of_kilograms_for_transportation = int(input("Enter required number of kilograms for transportation:  "))
        generating_a_random_number_of_passenger_cars()          
        generating_a_random_number_of_trucks_cars()
        if (sum_passendger(mylist_passenger)) > required_number_of_passenger_seats:
            print("The generated number of cars will provide such a number of passenger seats!")
        elif (sum_passendger(mylist_passenger)) < required_number_of_passenger_seats:
            print("Sorry. The generated number of cars will not be enough (")
        if(sum_weight(mylist_weight)) > required_number_of_kilograms_for_transportation:
            print("The generated number of trucks is enough to transport such a mass of cargo")
        elif (sum_weight(mylist_weight)) < required_number_of_kilograms_for_transportation:
            print("Sorry. The generated number of trucks will not be enough (")

answer()