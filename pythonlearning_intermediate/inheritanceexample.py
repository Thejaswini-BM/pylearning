class Child(object):

	# Constructor 
	def __init__(self, name): 
		self.name = name 

	# To get name 
	def getName(self): 
		return self.name 

	# To check if this person is student 
	def isStudent(self): 
		return False

# Derived class or Child class 
class Student(Child): 

	# True is returned 
	def isStudent(self): 
		return True


std = Child("Ram") 
print(std.getName(), std.isStudent()) 

# An Object of Student 
std = Student("Shivam") 
print(std.getName(), std.isStudent()) 
