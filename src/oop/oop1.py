# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #top level
    pass

class GroundVehicle(Vehicle): #attrs from Vehicle
    pass

class Car(GroundVehicle): #attrs from Vehicle & GroundVehicle
    pass

class Motorcycle(GroundVehicle): #attrs from Vehicle & GroundVehicle
    pass

class FlightVehicle(Vehicle): #attrs from Vehicle 
    pass

class Airplane(FlightVehicle): #attrs from Vehicle & FlightVehicle
    pass

class Starship(FlightVehicle): #attrs from Vehicle & FlightVehicle
    pass