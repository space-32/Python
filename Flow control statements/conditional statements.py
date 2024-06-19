#Flow control statements determine the order in which statements are executed in runtime

#Conditional Statements
#if block
#Syntax
#if condition:
      #code
if 1<2:
    print('yes')

if 1<2:
    print('first block')
    if 2>3:
        print('second block')
'''if 1>2: (outer condition)
    print('first block')
    if 2>3: (inner condition)
        print('second block')
if the outer condition is false and inner is true still the inner condition will not get executed'''

#if else
#if condition:
     #code
#else:
     #code

if 1<2:
    print('hi')
else:
    print('hello')

if 1>2:
    print('hi')
else:
    print('hello')

#if elif else
#if condition1:
    #code
#elif condition2:
    #code
#else:
    #code

if 3<4:
    print('yes')
elif 2>3:
    print('No')
else:
    print('else block')

if 3>4:
    print('yes')
elif 2>3:
    print('No')
else:
    print('else block')

#elif ladder
name='John'
if name=='Bob':
    print('hi bob')
elif name=='Sam':
    print('hi sam')
elif name=='Tina':
    print('hi tina')
elif name=='Mary':
    printt('hi mary')
elif name=='John':
    print("hi john")
else:
    print('what is your name?')

#check for numbers/handle numbers
#x=input('enter number')
#we use input fxn to take an input from user, input fxn takes default value as string therefore we need to mention data type
x=int(input('enter number:'))
if x==0:
    print(x,'is zero')
elif x%2==0:
    print(x,'is even no.')
else:
    print(x,'is odd no.')








