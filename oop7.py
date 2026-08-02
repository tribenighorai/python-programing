class Student:
     
    def __init__ (self,fullname,mark):
        self.name=fullname
        self.mark=mark
        print("adding new student id database..")
    
    #method define(normal nethod)
    def welcome(self):
        print("welcome student",self.name,self.mark)
    
    #satic method(not use "self" patametar)
    @staticmethod
    def hello():  
        print("hello all friends") 

s1=Student("Tribeni",67)
s1.welcome()
s1.hello()
