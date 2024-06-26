#Recurssive functionns are functions calling itself again and again
'''
e.g.
factorial(3)- 3*2*1
factorial(3)- 3* factorial(2)
factorial(2)- 2*factorial(1)
factorial(1)- 1*factorial(0)

factorial(n) - n* factorial(n-1)
'''


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(0))
print(factorial(3))
print(factorial(4))
