print("two numbers used for operation:")
a=int(input("enter first number:"))
b=int(input("enter second number:"))
choice=0
while choice<5:4
    print("calculator operator:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("5.Divide")
    print("5.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        c=a+b
        print("sum:",c)
    elif choice==2:
        c=a-b
        print("subtraction:",c)
    elif choice==3:
        c=a*b
        print("Multiplication:",c)
    elif choice==4:
        c=a/b
        print("division:",c)
    elif choice==5:
        break
    else:
        print("invalid choice")
