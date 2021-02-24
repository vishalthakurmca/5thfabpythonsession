print("Enter some Elments spreted by comma for a list")
mylist=[eval(e) for e in input().split(',')]
tupl=tuple(mylist)
print(tupl)
print(mylist)