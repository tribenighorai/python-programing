class Student:
    name="noname"
     
    def __init__ (self,fullname,mark):
        
        self.name=fullname
        self.mark=mark
        print("adding new student id database..")
        
s1=Student("Tribeni",67)
print(s1.name,s1.mark)
s2=Student("piu",89)
print(s2.name,s2.mark)
s3=Student()
print(s3.name,s3.mark)
print(Student.name)
