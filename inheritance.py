# create a base class Vehicle with a start method and then create a  Subclass Bike with an additional
# ride method and demonstrate how Bike can use both Start and Ride

class Vehicle:
    def __init__(self):
        pass

    def start(self):
        print("Start the Vehicle")

class Bike(Vehicle):
    def ride(self):
        print("Ride the bike")

vehicle = Bike()
vehicle.start()
vehicle.ride()