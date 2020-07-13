def div(a,b):
    return a/b

# new func 
def smartdiv(func):
    # inner func
    def inner(a,b): 
        if a<b:
            a,b = b,a
        return func()  
    return inner

 

# function call
result = smartdiv(div)
print(div(2,4))