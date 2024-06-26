#Types of function arguments

def add(a,b): #here a,b are formal arguments
    print(a+b)
add(4,5) #these are actual arguments

#Actual arguments are of 4 typed
#1. Positional arguments

def person(name,age):
    print(name)
    print(age)
person('John',30)
# person(23,'Sam') this will give as an o/p as name= 25 and age = sam but not an error to overcome this we can specify the arguments such as person(age=25, name="sam")
#here the order of the arguments dosen't matter

#2.Default arguments
def avg(a=10,b=20):
    c=(a+b)/2
    print(c)
avg() #now while calling if we don't give arguments it will take default arguments as a=10 and b=20
avg(30,20) # now since we mentioned the arguments it will take new values as a=20 and b=20


#Variable length argument

def sum(a,b,d,e):
    c=a+b+d+e
    print(c)
sum(2,3,5,6)

def sum(a,*b):#we are using * for multiple values
    c=a
    for i in b:
        c=c+i
        print(c)
        #3=3+4
        #7=7+5 and so on
sum(3,4,5,6,7)
#a is holding 3 and the remaining values will be in b so we have to iterate in order to add each value


#4.Keyword variable length arguments

def person(name,*data):
    print(name)
    print(data)
#person("John","delhi",30,98764) here the output is in tuple and it doesnot specifies what is what, like 30 is what, age? id? like that way
person('john',age=30,city='delhi',mob=98765)#here we are passing arguments and mentioning them so in such 


