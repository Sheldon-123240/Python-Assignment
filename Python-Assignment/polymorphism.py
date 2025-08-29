class Car:
    def move(self):
        return "Driving!"

class Bicycle:
    def move(self):
        return "Cycling!"

class Motorbike:
    def move(self):
        return "Riding!"

class Ship:
    def move(self):
        return "Sailing!"

class Pipeline:
    def move(self):
        return "Flowing!"

for vehicle in [Car(), Bicycle(), Motorbike(), Ship(), Pipeline()]:
    print(vehicle.move())
    
