class Dog:  
      
    # A simple class 
    # attribute 
    attr1 = "mamal"
    attr2 = "dog"
  
    #init method or constructor 
    def __init__(self,name):
        #instance variable
        self.name = name
        print("name is",self.name)
        
    
    # A sample method 
    def fun(self,age): 
        self.age = age
        print('age is',self.age)
        print("I'm a", self.attr1) 
        print("I'm a", self.attr2) 
        
# Creating object p1        
p1 = Dog('pug')
p1.fun(2)
# Class variables can be accessed using class name also 
print(Dog.attr1)
print(Dog.attr2)
# Class variables can be accessed using object p1 
print(p1.attr1)
