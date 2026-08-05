class Student:
    school="ABC school"

    def __init__(self,name):
        self.name=name

    @classmethod
    def pocha(cls, school_name):
        cls.school=school_name

s1=Student("Tribeni")
print(s1.name)
print(s1.school)

Student.pocha("XYZ school")
print(s1.school)
