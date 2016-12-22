class Vehicle():
    def __init__(self,make,model,year,mileage,price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def getmake(self):
        return self.make

    def setmake(self, make):
        self.make = make

    def getmodel(self):
        return self.model

    def setmodel(self,model):
        self.model = model

    def getyear(self):
        return self.year

    def setyear(self,year):
        self.year = year

    def getmileage(self):
        return self.mileage

    def setmileage(self,mileage):
        self.mileage = mileage

    def getprice(self):
        return self.price

    def setprice(self,price):
        self.price = price


    def display(self):
        print("Make:",self.make)
        print("Year:",self.year)
        print("Model:",self.model)
        print("Miles:",self.mileage)
        print("Price:",self.price)


class Car(Vehicle):

    def __init__(self,make,model,year,mileage,price,number_of_doors):

        super().__init__(make,model,year,mileage,price)

        self.number_of_doors = number_of_doors

    def getnumber_of_doors(self):
        return self.number_of_doors

    def setnumber_of_doors(self,number_of_doors):
        self.number_of_doors = number_of_doors

    def display(self):
        print("Inventory unit: Car")
        super().display()
        print("Number of Doors:",self.number_of_doors)

class Truck(Vehicle):

    def __init__(self,make,model,year,mileage,price,drive_type):

        super().__init__(make,model,year,mileage,price)

        self.drive_type = drive_type

    def getdrive_type(self):
        return self.drive_type

    def setdrivetype(self,drive_type):
        self.drive_type = self.drive_type

    def display(self):
        print("Inventory unit: Truck")
        super().display()
        print("Drive type:",self.drive_type)


class SUV(Vehicle):

    def __init__(self,make,model,year,mileage,price,passenger_capacity):

        super().__init__(make,model,year,mileage,price)

        self.passenger_capacity = passenger_capacity

    def getpassenger_capacity(self):
        return self.passenger_capacity

    def setdriver_capacity(self,passenger_capacity):
        self.passenger_capacity = passenger_capacity

    def display(self):
        print("Inventory unit: SUV")
        super().display()
        print("Pasenger capacity:",self.passenger_capacity)

class Inventory():

    def __init__(self):
        self.total = []

    def addVehicle(self,Vehicle):
        self.total.append(Vehicle)

    def display(self):

        for i in self.total:
            i.display()
            print()
        print()

def main():
    myinventory = Inventory()

    Continue = True

    while Continue == True:
        
        Type = input("Enter a vehicle type(Car/Truck/SUV): ")
        if Type.lower() == "car":
            Number_of_doors = int(input("Enter number of doors: "))
        elif Type.lower() == "truck":
            Drive_type = input("Enter a drive type: ")
        elif Type.lower() == "suv":
            Passenger_capacity = int(input("Enter passenger capacity: "))
        else:
            Continue = False
            
        Make = input("Enter a make: ")
        Year = int(input("Enter a year: "))
        Model = input("Enter a model: ")
        Miles = int(input("Enter number of miles: "))
        Price = int(input("Enter a price: "))

        if Type.lower() == "car":
            myvehicle = Car(Make,Year,Model,Miles,Price,Number_of_doors)

        elif Type.lower() == "truck":
            myvehicle = Truck(Make,Year,Model,Miles,Price,Drive_type)
        elif Type.lower() == "suv":
            myvehicle = SUV(Make,Year,Model,Miles,Price,Passenger_capacity)
        else:
            pass

        myinventory.addVehicle(myvehicle)

    
        repeat = input("Would you like to enter another vehicle (Y/N)?: ")
        if repeat.lower() == "y":
            Continue = True
        else:
            Continue = False


    myinventory.display()



main()          
