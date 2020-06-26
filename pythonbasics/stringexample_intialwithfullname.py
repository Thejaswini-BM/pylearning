#printing the intials of name with last name in fullname
def fullname(name):
    splitsting = name.split()
    new = ""
    for i in range(len(splitsting)-1):
        name = splitsting[i]
        new += (name[0].upper()+'.') 
    new += splitsting[-1].title()
    return new

name = 'tejaswini bitanahalli muniraju'
print(fullname(name))    
        
