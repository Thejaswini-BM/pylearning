# Python program to demonstrate 
# multiple inheritance 


# Base class1 
class Mother: 
	 
	def mother(self,name): 
		self.name = name
         

# Base class2 
class Father: 
	 
	def father(self,age): 
		self.age = age
         

# Derived class 
class Son(Mother, Father): 
	def parents(self): 
		print("Father's age :", self.age) 
		print("Mother name :", self.name) 

# Driver's code 
s1 = Son() 
s1.mother('sita')
s1.father(24)
s1.parents() 
