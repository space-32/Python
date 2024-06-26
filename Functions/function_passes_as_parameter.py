#Function passes as parameter to another function

def display(fun):
    return "Hi" + fun

def name():
    return 'sam'
print(display(name())) #we can pass the another function in one function


def display(fun):
    return "Hi" + fun

def name(arg):
    return 'sam' + arg
print(display(name('How are you')))

#Assign functions to variables
a=11#global
def display():
    a=12 #local
    print(a)
    print(globals()['a'])
print(a)
z=display #assigning variable to function
z()
#calling/invoking function through variable



#Nested Function
def outer_function(fun):
    def inner_function():
        return 'Hi' + fun
    return inner_function()
print(outer_function("John"))


def outer_function():
    def inner_function(arg):
        return 'Hi' + arg
    return inner_function('Sam')
print(outer_function())


def outer_function(fun):
    def inner_function(arg):
        return 'Hi' + fun +arg
    return inner_function('whatsup?')
print(outer_function("John,"))

def outer_function():
    def inner_function():
        return 'Hi'
    return inner_function()
print(outer_function())


#passing sequence types to function
def myfunc(lst):
    for i in lst:
        print(i)
myfunc([1,2,3])