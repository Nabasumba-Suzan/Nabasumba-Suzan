class Device:
    def info(self):
        print("This is an electronic device.")

class Phone(Device):
    def info(self):
        print("This is a phone.")

class SmartPhone(Phone, Device):
    pass

sp = SmartPhone()
sp.info()


print(SmartPhone.__mro__)
