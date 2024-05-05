# Create a Bus child class that inherits from the Vehicle class. The default
# fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance
# charge. So total fare for bus instance will become the final amount = total
# fare + 10% of the total fare.
# Example:
# Vehicle Fare: 5000
# Bus Fare: 5500.0

class Vehicle:
    def __init__(self,seat_capacity):
        self.seat_capacity = seat_capacity
    def get_fare(self):
        return self.seat_capacity * 100
    
class Bus(Vehicle):
    def __init__(self,seat_capacity):
        super().__init__(seat_capacity)
    def get_fare(self):
        vehicle_fare = super().get_fare()
        maintainence_fare = 0.1 * vehicle_fare
        total_fare = vehicle_fare + maintainence_fare
        return total_fare
    
Vehicle1 = Vehicle(50)
print("Vehicle fair:",Vehicle1.get_fare())

Bus1 = Bus(50)
print("Bus fair:",Bus1.get_fare())