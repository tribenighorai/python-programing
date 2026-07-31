class Student:
	school_name="abc_school"
	
	def __init__ (self, name, roll):
		self.name= name
		self.roll= roll

s1= Student (" Tribeni ", 45)
print(s1.name, s1.roll,s1.school_name)
s2=Student ("piu",78)
print(s2.name,s2.roll,s2.school_name)
