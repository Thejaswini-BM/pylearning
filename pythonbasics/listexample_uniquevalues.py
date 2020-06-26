# getting unique values from list

def uniquevalues(list1):
    uniquelist = []
    for x in list1:
        if x not in uniquelist:
            uniquelist.append(x)
    for x in uniquelist:
        print(x)
list1 = [1,2,3,4,5,3,4,5,7]
uniquevalues(list1)  
      