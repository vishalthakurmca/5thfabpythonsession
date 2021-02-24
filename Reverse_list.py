def reverse_list(l1):
    final_list=[]
    for i in l1[-1::-1]:
        final_list.append(i)
    return final_list

mylist=[1,2,3,4,5]
print(reverse_list(mylist))