class Greeting: 

	# default constructor 
	def __init__(self): 
		self.greet = 'hello'

	# a method for printing data members 
	def print_Greeting(self): 
		print(self.greet) 


# creating object of the class 
obj = Greeting() 

# calling the instance method using the object obj 
obj.print_Greeting() 
