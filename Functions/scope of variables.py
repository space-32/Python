#Scope of variables
#1. Global variable
#2.Local variable

x=123  #global variable
def display():
    y=456 #Local variable
    print(y)
    print(x)
print(x)
display()

#Access global variable with same name
a=11#global variable
def display():
    a=22
    print(a)
    print(a)
    print(globals()['a'])
print(a)
display()
