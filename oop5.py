class Student:
     
    def __init__ (self,fullname,mark):
        
        self.name=fullname
        self.mark=mark
        print("adding new student id database..")
    #method define
    def welcome(self):
        print("welcome student",self.name,self.mark)
   
s1=Student("Tribeni",67)
s1.welcome()
#print(s1.name,s1.mark)
s2=Student("piu",89)
s2.welcome()
#print(s2.name,s2.mark)
