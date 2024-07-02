contact={}

def display():
    print("name\t\t Phone Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:

    choice=int(input("1. Add contact \n 2. Search contact \n 3.Display contact \n 4.Delete Contact \n 5. Exit \n enter your choice:"))

    if choice==1:
        name=input("enter the name:")
        ph_number=input("enter the mobile number:")
        contact[name]=ph_number
    elif choice==2:
        search_name=input("enter the name to be search:")
        if search_name in contact:
            print(search_name,"'s mobile number is:",contact[search_name])
        else:
            print("Contact name is not in the contact list")
    elif choice==3:
        if not contact:
            print("NO CONTACT")
        else:
            display()
    elif choice==4:
        delete_contact=input("enter the contact to be deleted:")
        if delete_contact in contact:
            confirm = input("Do you want to delete it y/n?")
            if confirm=="y" or confirm=="Y":
                contact.pop(delete_contact)
            display()
        else:
            print("Contact name is not in the contact list")
    else:
        break
