class Car:
    colour="black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

class ToyotoCar(Car):
    def __init__(self,name):
        self.name=name
        
class Fortunar(ToyotoCar):
    def __init__(self,type):
        self.type=type
    
c1=Fortunar("desal")
print(c1.type)
print(c1.colour)
c1.stop ()

