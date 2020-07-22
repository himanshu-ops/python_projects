#!/home/him/anaconda3/bin/ipython3

loop = 1 

choice = 0

while loop == 1:
    print("Welcome to calc.py")

    print("your options are")

    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit calculator")

    choice = int(input("Choose your option: "))
    if choice == 1:
        add1 = int(input("Add this: "))
        add2 = int(input("to this: "))
        print (add1, "+", add2, "=", add1 + add2)
    elif choice == 2:
        sub2 = int(input("Subtract this: "))
        sub1 = int(input("from this: "))
        print (sub1, "-", sub2, "=", sub1 - sub2)
    elif choice == 5:
        loop = 0

print ("Thankyou for using calculator.py!")
