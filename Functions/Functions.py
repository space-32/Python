#Functions are group of statements that performs particular tasks
#Functions can be built in or user define
#Functions may or may not have arguments.

#Syntax of Function
#def function_name():
     #Function body (code/statement)
#function_name()

def greet():
    print('hi')
    print('hello')
greet()
#can call function as much time as we want

#Add 2 no.
def add(a,b):
    c=a+b
    print(c)
add(2,3)

#Function to find avg of 2 no.
def avg(a,b):
    print("Avg of 2 no. is",(a+b)/2)
avg(10,20)


#functions can return back result

#Function that return addition of 2 numbers
def add(a,b):
    return a+b
    #if we are storing a+b in any variable then return that variable. e.g c=a+b then return c
#when we use the return we need to use the print fxn or else there will be no o/p
print(add(3,4))


#Function can return multiple values
def cal(a,b):
    x=a+b
    y=a-b
    c=a*b
    d=a/b
    return x,y,c,d
print(cal(10,5)) #will return the o/p in the form of tuple
result=cal(10,5)
for i in result:
    print(i)#now o/p is not in tuple format
for i in cal(10,5):
    print(i)#other method

