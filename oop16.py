class Car:
    colour="black"
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

class ToyotoCar(Car):
    def __init__(self,name,type):
        self.name=name
        super(). __init__(type)

car1=ToyotoCar("prius","electric")
print(car1.name)
print(car1.type)
print(car1.colour)
car1.start()
