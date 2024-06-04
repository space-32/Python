#variables are box/containers to store the values

a=10
print(a)

a='John'
print(a)


pi=3.14
print(pi)
print(id(pi))# find the id of the varibale in memory
print(type(pi))# prints the type pf the varible e.g int,float etc




'''types of variables assignment
There are 2 types of variable assignment
1.Multiple variable, single assignment
2.multiple varibles and multiple assignment'''


#1. Multiple variable, single assignment
a=b=c=5
print(a)
print(b)
print(c)


#multiple varibles and multiple assignment
x=10
y=20
z=30
#or
x,y,z=10,20,30
# these 2 are valid syntax for multiple variable multiple assignments
# invalid syntax is assigning values in one line
# x=10,y=20,z=30
print(x,y,z)


#values and type
a=10
print(a)
print(type(a))

#scope of variables(in detail in functions)
#1.Global variable
#2. Local variable
