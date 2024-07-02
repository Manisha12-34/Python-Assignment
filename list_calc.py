def sum_of_list(list):
    temp=0
    for i in list:
        temp=temp+i
    return temp

list_length = int(input("enter list length:"))
my_list=[]
for _ in range(list_length):
    temp=int(input("enter the numbers:"))
    my_list.append(temp)

sum=sum_of_list(my_list)
print("sum of the number present in list: ",sum)