class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting the car with a key...")  # Overrides Vehicle.start()

v = Vehicle()
v.start()

c = Car()
c.start()
