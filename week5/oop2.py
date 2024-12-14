# Base Class: Vehicle
class Vehicle:
    def move(self):
        return "The vehicle moves."

# Derived Class: Car
class Car(Vehicle):
    def move(self):
        return "The car drives on roads. 🚗"

# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        return "The plane flies in the sky. ✈️"

# Derived Class: Boat
class Boat(Vehicle):
    def move(self):
        return "The boat sails on water. 🚤"

# Example Usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
