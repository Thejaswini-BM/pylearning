def outer():
    x = 5
    # inner func
    def inner():
        y = 3
        print (x+y)
    return inner

r = outer()
print(r.__name__)
g = r
print(g)


