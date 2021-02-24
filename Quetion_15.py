def sum_of_evennum(num):
    sam=0
    for i in range(1,num+1,1):
        if i%2==0:
            sam=sam+i
    return sam
num=int(input("Enter a Number"))
print(sum_of_evennum(num))