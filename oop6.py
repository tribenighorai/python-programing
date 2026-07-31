class Student:
    name="noname"
     
    def __init__ (self,fullname,mark):
        
        self.name=fullname
        self.mark=mark
        print("adding new student id database..")
    #method define
    def welcome(self):
        print("welcome student",self.name,self.mark)
    #this is another method(which is return the mark)
    def gate_mark(self):
        return self.mark
s1=Student("Tribeni",67)
s1.welcome()
#print(s1.name,s1.mark)
s2=Student("piu",89)
s2.welcome()
#print(s2.name,s2.mark)
s2.gate_mark()
print(s2.gate_mark)
