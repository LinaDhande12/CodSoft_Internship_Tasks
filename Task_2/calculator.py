
x = int(input("Enter 1st integer no : "))
y = int(input("Enter 2nd integer no : "))

def validation(x,y):
    if x >= 0 and y >= 0:
        print("Valid integers ")
        return True
    else:
        print("please Enter valid integers...")
        return False
    
    

def add(x,y):
    if validation(x,y):
        c = x+y
        print(f"Addition of {x} and {y} is {c} ")

def sub(x,y):
    if validation(x,y):
        d= x-y
        print(f"Subtraction of {x} and {y} is {d}")

def mul(x,y):
    if validation(x,y):
        e = x*y 
        print(f"Multiplication of {x} and {y} is {e}")

def div(x,y):
    if validation(x,y):
        if y == 0:
            print("cannot divide by zero .\n")
        else:
            f = x/y
            print(f"Division of {x} and {y} is {f}")

def mod(x,y):
    if validation(x,y):
        if y == 0:
            print("cannot perform modulus by zero.\n")
        else:
            g = x%y
            print(f"Modulus of {x} and {y} is {g}")

 
# Main loop
while True:
    
    print("------------MINI CALCULATOR-------------\n")
    print("1. Addition of Two nos ")
    print("2. Subtraction of Two nos ")
    print("3. Multiplication of Two nos")
    print("4. Division of Two nos ")
    print("5. Modulus of Two nos ")
    print("6. Exit\n")

    choice = input("Enter your choice to perform Arithmetic operations : ")
    
    if choice == "1":
        add(x,y)
    elif choice == "2":
        sub(x,y)
    elif choice == "3":
        mul(x,y)
    elif choice == "4":
        div(x,y)
    elif choice == "5":
        mod(x,y)
    elif choice == "6":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.\n")
