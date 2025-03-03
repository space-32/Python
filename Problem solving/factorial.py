#write a program to calculate factorial of a number using while loop

n=int(input("Enter a number:"))
fact=1
i=n
if n<0:
    print("Factorial is not defined for negative numbers")
elif n==0 or n==1:
    print(f"Factorial of {n} is 1")
else:
    while i>1:
        fact *= i
        i -= 1
    print(f"Factorial of {n} is {fact}")
