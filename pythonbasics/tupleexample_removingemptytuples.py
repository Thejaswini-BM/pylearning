# removing empty tuples from list
def removedup(tuples):
    tuples = [ t for t in tuples if t]
    return tuples
          
tuples = [(), ('Hello','15','8'), (), ('World', 'sita'), ('Python', 'Program', '45'), ('',''),()]
print(removedup(tuples))
          