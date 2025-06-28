class Device:
    def info(self):
        print("This is an electronic device.")

class Phone(Device):
    def info(self):
        print("This is a phone.")

class SmartPhone(Phone, Device):
    def info(self):
        Device.info(self)
        Phone.info(self)

sp = SmartPhone()
sp.info()



