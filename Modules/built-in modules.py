#Modules that are already present in python

import platform
z=platform.system()
print(z)

#Find the area of a circle
#area =pi * r**2
'''import math
r=float(input("Enter a radiues:"))
area=r*math.pi**2
print(area)'''
#print(math.pi)

#from math import pi
#print(pi) #here we importing a specific function as pi so no need to mention math.pi

from math import *
#asterisk bcz we want to importing everything from math
print(pi)
print(factorial(3))
print(sqrt(23))

#dir() - use to know what functions are there in math module
import math
print(dir(math))

#random module - will generate random numbers, we just have to specify the range
import random
print(random.randint(0,5)) #inclusive of both 0 and 5 since it is not range fxn
print(random.random())
print(random.random()*100)
print(dir(random))