def captlize_list(l1):
    f_list=[]
    for i in l1:
        f_list.append(i.capitalize())
    return f_list

mylist=['vishal','raj','thakur','kumar']
print(captlize_list(mylist))