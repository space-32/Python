#for loops

#syntax of for loop
#for item in seq:
     #code
mylist=[1,2,3,4,5]
for i in mylist:
    print(i)

#print even no.in mylist
for j in mylist:
    if j%2==0:
        print(j,'is even')
    else:
        print(j,'is odd')

#sum up elements in mylist
list_sum=0
for i in mylist:
    list_sum=list_sum+i
    print(list_sum)
    #0=0+1
    #1=1+2
    #3=3+3
    #6=6+4 and so on

#iterate over strings
mystr='hello world'
for letter in mystr:
    print(letter)
#for output to be in horizontal
mystr='hello world'
for letter in mystr:
    print(letter,end=' ')
print()#it will end the iteration and will not join the very next statement of the code

for letter in 'python':
    print('hi')

#iterate over tuples
tpl=(1,2,3)
for i in tpl:
    print(i)


#iterate over sets
s1={1,2,3}
for i in s1:
    print(i)

#iterate over dict
d1={1:10,2:20,3:30}
for i in d1:
    print(i)
    print(d1[i])

for k in d1.keys():
    print(k)

for v in d1.values():
    print(v)

for x,y in d1.items():
    print(x,y)

#display no. form 50 to 70
#range fxn
for i in range(50,70):
    print(i,end=' ')
print()#so that outputs wont overlap
#inclusive of 50 but exclusive of 70

for i in range(50,70,2):
    print(i,end=' ')
print()
#interval of 2,print alternate no., 2 dosen't mean even no. it is alternate no.


#print a multiplication table of a no.
x=int(input("enter a no."))
for i in range(1,11): #1 inclde, 11 exclude
    print(i*x)
for i in range(1,11):
    print(x,"X",i,'=',i*x)
print()









