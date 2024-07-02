a=int(input("enter a number: "))
print("multiplication of table a is:")
try:
    for i in range(1, 11):
        print(a, 'x', i, '=', a*i)

except:
    print("Invalid input!!")

print("Hello, this is to show error is handled")