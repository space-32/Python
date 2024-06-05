#Strings are sequence of characters and enclosed in single or double quotes
#Display string using print()

print('Hello')
print("Hello")

#Assign string to variable
s='Python' #single line str
print(s)
print(type(s))

s1="Python is easy to learn than JAVA"
print(s1)
print(type(s1))

s1="Python is easy \n to learn than JAVA"
#\n will display the str in next line, 1st approach
print(s1)
print(type(s1))

s1='''Python is easy
     to learn than JAVA'''
# 2nd approach
print(s1)
print(type(s1))


#str indexing
#Indexing in py starts from 0 and goes upto n-1
s="Python is easy"
print(s[0])# will give the o/p as the P since its at index 0
print(s[6])#it'll give o/p as space bcz it is also a character

#Slicing
print(s[0:5])#inclusive of 0 and exclusive of 5
print(s[0:6])
print(s[:4])#if we don't specify the start it will automatically starts from 0
# and if we are specifying the start and not end then it'll print everything
#and if we don't specify both start and end then it'll print everything
print(s[-3:-1])
#we can also give -ve indexing

'''print(s[-1:-3])
this will not give the o/p since -1 is greater than -3, starting index should be minimum in -ve indexing'''


#steps values to slice
print(s[0:9])
print(s[0:9:2]) #here, 2 is step value, it means it'll skip by 2
#the o/p will be = Pto s, why P bcz starting index is 0 and ending index is 9 with inclusion of space

#Repetition
print(s*2)
#will print s 2 times

#Length of string
print(len(s))# will print the length including spaces

#String Methods
#Python has support for built in methods for string
#1.strip()
m='  You are awesome  '
print(m)
print(m.strip())
print(m.lstrip()) #remove space form L.H.S.
print(m.rstrip()) #removes spaces from R.H.S.


#2.find()
print(m.find('are'))#will return the index position of a

#count()
print(m.count('e'))
print(m.count('a'))#here o/p will be 1 bcz lowercase a is 1 time, since py is case sensitive

#replace()- replaces main str with new substring
print(m.replace('awesome','Cool'))
print(m)#it will give both you are cool & you are awesome; we are not storing it back in variable therefore this o/p

#upper(),lower(),title()
print(m.upper())
print(m.lower())
print(m.title())#1st word will be in caps

#split()
a="Hellow,World"
print(a.split(','))

print(m.isdigit())#it will check m is digit or not if yes will return True else False
print(m.startswith('Y'))#from which letter the string is starting if the mentioned character is correct then return True else false
print(m.endswith(' '))
print(m.swapcase())#swapping of lowecase with uppercase and vice versa
print(m.capitalize())#1st letter caps


#check the string-'in' and 'not in'
txt='No gain without pain'
print('ain'in txt)
print('aing' in txt)
print('no' not in txt)


#string concatenation
x='Hello'
y='World'
print(x+y)
print(x+' '+y)
#we can concate only string with string
#if we want to concat some other data type in str the do type casting to it
'''x='hello'+100
print(x) will give error'''
x='hello'+str(100)#type casted int to str
print(x)#will give o/p

#format()
age=10
txt='My name is sam and I am {}'
print(txt.format(age))

#strings are immutable