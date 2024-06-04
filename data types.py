'''DATA TYPES

Python supports wide range of data types like integers, floating point numbers, complex numbers,
• Boolean Built in data types known as Sequences/Collections.
• Data types represents the type of data stored into variable of memory.
• The data types already available in python language are called Built-in data types.
• The data types which are created by the programmers are called User-defined data types.'''


#1. None
a=None
print(a)
print(type(a))

'''Numeric Types
It has 4 types
1. integer(int)
2.float
3.complex
4.Boolean'''

a=10  #int
print(a)
print(type(a))

x=10.90  #float
print(x)
print(type(x))


c=2+3j  #complex no.
#for imaginary no. the "j" is the standard coefficient, if we use an i in the place of j it'll throw an error
print(c)
print(type(c))


# Boolean type either return True of False
d=True
print(d)
print(type(d))
#Here, if we use lowecase t for True and lowercase f for False then it'll throw an error
# same code for False
print(4>3)
# it'll return the value as True bcz condition is true
print(type(4>3))
#will return the class<bool> and not the value True


'''String  Type
 It can be defined in single quotation or double quotation
even if no. is define in double or single quotation then it is treated as string not no.'''

s='Python is easy'
print(s)
print(type(s))

v='100' # Numerical string
print(v)
print(type(v))

#Represent no. in diff formats
print(bin(10))# will print the no. in binary
print(oct(10))#will print the no. in octal
print(hex(10))# will print the no. in hexadecimal

'''Type casting/Type conversion
Converts one data type to another data type
Type Conversion is also known as Type casting.
• It is used to convert data type of variable.
• Example: Convert floating point number to integer number.
x = 12.5
print X)
print(type(x))
y = int(x)
print(y
print(type(y))'''
#1.Convert int into float
u=8
print(u)
print(type(u))
y=float(u)
print(y)
print(type(y))

#2.Convert string into int
'''n='Python'
print(n)
print(type(n))
t=int(n)
print(t)
print(type(t))'''
#this above code will throw an error bcz the str we have is of characters and not of no.

n='100'
print(n)
print(type(n))
t=int(n)
print(t)
print(type(t))
#this code will give the o/p


#3.Convert complex to int
'''m=2+3j
print(m)
print(type(m))
b=int(m)
print(b)
print(type(b))'''
#this code will throw an error since the conversion of complex to float or int is not possible


#4. int to complex
j=3
print(j)
print(type(j))
i=complex(j)
print(i)
print(type(i))
# conversion of int to complex is possible

'''Mutable and Immutable objects
Mutable Object= These types can be changed.e.g. Lists, set, dictionary
Immutable Objects= cannot be chaged or modified, e.g. int,float,boolean, str,tuples'''
