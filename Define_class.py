class test:
    def __init__(self):
        self.str=str
    def getstring(self,str):
        self.str=str
    def printstring(self,str):
        print(self.str.upper())
f1=test()
str=input("Enter a strng")
f1.getstring(str)
f1.printstring(str)