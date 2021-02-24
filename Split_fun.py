print("Enter names sparted with comma")
mylist=[]
for e in input().split(','):
    mylist.append(e)
    mylist.sort()
for i in mylist:
    print(i.upper(),end=",")