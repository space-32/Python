num = int(input("Enter a Number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:  # This else belongs to the for-loop, executed only if no break occurs
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
