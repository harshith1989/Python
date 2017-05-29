

def accept_input():
    while 1:
        try:
            a = float(input("\nPlease enter numerical value for variable a : "))
        except ValueError:
            print("Not an number!")
            continue
        else:
            break
    while 1:
        try:
            b = float(input("\nPlease enter numerical value for variable b : "))
        except ValueError:
            print("Not an number!")
            continue
        else:
            break


    return a, b


def add():
    a, b = accept_input();
    print("\nThe sum of the 2 numbers {} & {} is : {}\n\n".format(a,b,a+b))
    return a + b

def subtract():
    a, b = accept_input();
    print("\nThe sum of the 2 numbers {} & {} is : {}\n\n".format(a,b,a-b))
    return a - b

def multiply():
    a, b = accept_input();
    print("\nThe sum of the 2 numbers {} & {} is : {}\n\n".format(a,b,a*b))
    return a * b

def divide():
    a, b = accept_input();
    print("\nThe sum of the 2 numbers {} & {} is : {}\n\n".format(a,b,a/b))
    return a / b


choices = ("1", "2", "3", "4")
name = input("Please enter name : ")
print(f"\nHello {name} !!\n")

while 1:

    print(" - Type 1 for addition")
    print(" - Type 2 for subtraction")
    print(" - Type 3 for multiplication")
    print(" - Type 4 for division")
    print(" - Type anything else to abort")
    choice = input("\nPlease type-in the required operation : ")

    if choice in choices:
        print("Processing...")
    else:
        print(f"\nThank you {name}, Goodbye! ")
        break


    if int(choice) == 1:
        add()
    elif int(choice) == 2:
        subtract()
    elif int(choice) == 3:
        multiply()
    else:
        divide()

    print("*************************************************************\n")


