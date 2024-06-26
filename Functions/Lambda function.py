#Lambda functions are small anonymous functions
#Lambda functions can take any number of arguments but one single expression
#Syntax
#Lambda arg_list : expression

def result(n):
    return n*n
print(result(2))

#above function in lambda

f=lambda n:n*n
print(f(2))

#lambda to add 2 no.
f= lambda a,b:a+b
print(f(10,20))

#Lambda to join joints
s=lambda s1,s2:s1+s2
print(s('hello','world'))

#lambda to multiply 3 no.
z=lambda a,b,c:a*b*c
print(z(1,2,3))


#Lambda function methods
#filter() - filters out sequence elements based on ssome logic and condition
#filter(lambda function,iterable)
#Retreive only even no. from list of given no.
lst=[1,2,3,4,5]
reuslt=(filter(lambda x:x%2==0,lst))
print(result)

lst=[1,2,3,4,5]
result=list(filter(lambda x:x%2==0,lst)) #typecasting output into list
print(result)

#map() - maps out the sequence elements based on some condition and logic
#map(lambda function,iterable)

#given list of numbers double each list of elemnents
lst=[1,2,3,4,5]
result=list(map(lambda x:x*2,lst))
print(result)


#reduce()-reduces sequence elements to one single value based on condition and logic
#reduce(lambda function,iterable)

#import reduce using -

from functools import reduce
#given list of elements sum up list of elemnets
lst=[5,10,4,2]
result=reduce(lambda x,y:x+y,lst)
print(result)






