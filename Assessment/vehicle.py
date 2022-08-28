#Using your knowledge of OOP, write the inheritance hierarchy for all the types of vehicles that you know. 
# The top level class should be Vehicle. Structure your hierarchy as much as possible to give it 
#as many levels as possible. Your vehicle class must be created with a name, mileage and capacity attributes.
#From above, add a method to add passenger, to remove passenger, to return total number of 
#passengers and to calculate total fare based on number of passengers.


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        
    def get_name(self):
        return self.name
    
    def get_mileage(self):
        return f'{self.mileage} kmpl'
    
    def get_capacity(self):
        return self.capacity
    
    def add_passenger(self):
        self .capacity = self.capacity + 1
        return f'The number of passengers are now {self.capacity}'
    
    def remove_passenger(self):
        self.capacity = self.capacity - 1
        return f'The number of passengers are now {self.capacity}'
    
    def total_numof_passengers(self):
        total_num_of_passen = self.capacity
        return total_num_of_passen


class Land(Vehicle):
    def __init__(self, name, mileage, capacity, tfare):
        super().__init__(name, mileage, capacity)
        self.tfare = tfare
        
    def get_tfare_per_person(self):
        return self.tfare
        
    def total_tfare(self):
        return self.capacity * self.tfare
        
        
class Bus(Land):
    def __init__(self, name, mileage=4.50, capacity=18, tfare=2000):
        super().__init__(name, mileage, capacity, tfare)
        
class Car(Land):
    def __init__(self, name, mileage=12.50, capacity=5, tfare=2500):
        super().__init__(name, mileage, capacity, tfare)
        
class Train(Land):
    def __init__(self, name, mileage=0.16, capacity=700, tfare=3000):
        super().__init__(name, mileage, capacity, tfare)
        
class Van(Land):
    def __init__(self, name, mileage=7.60, capacity=950, tfare=50):
        super().__init__(name, mileage, capacity, tfare)
        
class Truck(Land):
    def __init__(self, name, mileage=15.00, capacity=50, tfare=1000):
        super().__init__(name, mileage, capacity, tfare)
        
class Motorcycle(Land):
    def __init__(self, name, mileage=62.50, capacity=2, tfare=200):
        super().__init__(name, mileage, capacity, tfare)
        
class Bicycle(Land):
    def __init__(self, name, mileage=20.00, capacity=1, tfare=0):
        super().__init__(name, mileage, capacity, tfare)
        

class Air(Vehicle):
    def __init__(self, name, mileage, capacity, tfare):
        super().__init__(name, mileage, capacity)
        self.tfare = tfare
        
    def get_tfare_per_person(self):
        return self.tfare
    
    def total_tfare(self):
        return self.capacity * self.tfare

class Aeroplane(Air):
    def __init__(self, name, mileage=0.24, capacity=500, tfare=50000):
        super().__init__(name, mileage, capacity, tfare)
        
class  Helicopter(Air):
    def __init__(self, name, mileage=5.50, capacity=10, tfare= 60000):
        super().__init__(name, mileage, capacity, tfare)
        

class  Water(Vehicle):
    def __init__(self, name, mileage, capacity, tfare):
        super().__init__(name, mileage, capacity)
        self.tfare = tfare
        
    def get_tfare_per_person(self):
        return self.tfare
    
    def total_tfare(self):
        return self.capacity * self.tfare
        
class Boat(Water):
    def __init__(self, name, mileage=0.85, capacity=150, tfare=10000):
        super().__init__(name, mileage, capacity, tfare)
        
class Ship( Water):
    def __init__(self, name, mileage=0.04, capacity=3000, tfare=10000):
        super().__init__(name, mileage, capacity, tfare)
        
        
        
        
bus1 = Bus("Honda")
print(bus1.get_name())
car1 = Car("Toyota")
print(car1.get_mileage())
train1 = Train("Huyunda")
print(train1.get_capacity())
truck1 = Truck("Landa")
print(truck1.add_passenger())
van1 =  Van("Boiler")
print(van1.remove_passenger())
motorcycle1= Motorcycle('Bajaj')
print(motorcycle1.total_numof_passengers())
plane1 = Aeroplane("Airpeace")
print(plane1.get_tfare_per_person())
ship1 = Ship("Adamac")
print(ship1.total_tfare())