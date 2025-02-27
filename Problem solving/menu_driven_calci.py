def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by 0"  # Return a string instead of printing

while True:
    print("\nMenu:")
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Exit")

    choice = input("Enter your choice of Operation: ")

    if choice == "5":
        print("Exiting from Program")
        break

    # Move input for numbers here, so they are taken after choice selection
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result: ", add(a, b))
    elif choice == "2":
        print("Result: ", sub(a, b))
    elif choice == "3":
        print("Result: ", multiply(a, b))
    elif choice == "4":
        print("Result: ", division(a, b))
    else:
        print("Enter a valid choice")
