class Cars():
    colors = ["red","blue","black","white"]
    complete_set=["budget","average","full"]
    
class Passenger_cars(Cars):
    number_of_passenger_seats = 5
    
class Trucks(Cars):
    weight = 1500
    maximum_cargo_dimensions = 1500*4000*1700
    

volga = Passenger_cars()
print(volga.number_of_passenger_seats,volga.colors)
zil = Trucks()
print(zil.weight,zil.colors)