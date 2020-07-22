#!/home/him/anaconda3/bin/ipython3

def menu():
    print("Welcome to calculator.py")
    print("your options are:")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit calculator.py")
    print(" ")
    return int(input("Choose your option: "))

def add(a,b):
    print (a, "+", b, "=",a + b)

def sub(a,b):
    print (b, "-", a, "=", b - a)

def mul(a,b):
    print (a, "*", b, "=", a * b)

def div(a,b):
    print (a, "/", b, "=", a / b)

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(int(input("Add this: ")),int(input("to this: ")))
    elif choice == 2:
        sub(int(input("Subtract this: ")),int(input("from this: ")))
    elif choice == 3:
        mul(int(input("Multiply this: ")),int(input("by this: ")))
    elif choice == 4:
        div(int(input("Divide this: ")),int(input("by this: ")))
    elif choice == 5:
        loop = 0

print ("Thank you for using calculator.py!")
