# difference between two list

def twolist(list1,list2):
    return (list(set(list1)-set(list2)))

list1 = [10,25,30,45,50,65]
list2 = [30,45,50]
print(twolist(list1, list2))

