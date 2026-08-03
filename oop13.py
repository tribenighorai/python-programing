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
        
c1=ToyotoCar("fortunar")
print(c1.name)
print(c1.start())
print(c1.colour)
