class Person:
    __name="anoname"
    
    def __hello(self):
        print("hello Person")
        
    def welcome(self):
        self.__hello()
        print(self.__name)

p1=Person()
#p1.__name
p1.welcome()
