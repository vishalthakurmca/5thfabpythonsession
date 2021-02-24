def sum_of_numbers(a):
    sam=0
    for i in range(1,a+1,1):
        sam=i+sam
    return sam
num=int(input("Enter a Number"))
print(sum_of_numbers(num))        