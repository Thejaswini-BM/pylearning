# Python program to demonstrate 
# multilevel inheritance 


# Base class 
class Grandfather: 
	grandfathername ="" 
	def grandfather(self): 
		print(self.grandfathername) 

# Intermediate class 
class Father(Grandfather): 
	fathername = "" 
	def father(self): 
		print(self.fathername) 

# Derived class 
class Son(Father): 
	def parent(self): 
		print("GrandFather :", self.grandfathername) 
		print("Father :", self.fathername) 


s1 = Son() 
s1.grandfathername = "aaa"
s1.fathername = "bbb"
s1.parent() 
