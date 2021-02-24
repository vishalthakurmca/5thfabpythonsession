for i in range(0,101,1):
    if(i%2==0):
        print(i,end=" ")
print("\n")

for i in range(0,101,1):
    if(i%2!=0):
        print(i,end=" ")
print("\n")
sum=0
for i in range(0,101,1):
    sum=sum+i
print("sum of 100 is",sum)