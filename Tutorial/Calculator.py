

def accept_input():
    a = float(input("\nPlease enter variable a : "))
    b = float(input("Please enter variable b : "))
    return (a,b)


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


name = input("Please enter name : ")
print(f"\nHello {name} !!\n")

while 1:

    print(" - Type 1 for addition")
    print(" - Type 2 for subtraction")
    print(" - Type 3 for multiplication")
    print(" - Type 4 for division")
    print(" - Type anything else to abort")
    choice = int(input("\nPlease type-in the required operation : "))

    if choice == 1 :
        add()
    elif choice == 2 :
        subtract()
    elif choice == 3 :
        multiply()
    elif choice == 4 :
        divide()
    else :
        print(f"\nThank you {name}, Goodbye! ")
        break

    print("*************************************************************\n")


