class Student:

    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
       

    def parcentage(self):
        self.par=(self.phy+self.chem+self.math)/3
        print(self.par)

S1=Student(98,99,89)
print(S1.parcentage())
