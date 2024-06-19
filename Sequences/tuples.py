#Tuples are sequences which are ordered indexed and immutable
#tuples are  written using ()
#We cannot perform methods such as append(),remove(),clear() etc since tuples are immutable

tpl=()
print(tpl)
print(type(tpl))

tpl=(40,) #in tuple the element should follow by , then it'll give output of type as tuple
print(tpl)
print(type(tpl))

tpl=(40,50,40,'xyz')
print(tpl)
print(type(tpl))

#repetition
print(tpl*3)

#length of tuple
print(len(tpl))

#indexing- it starts from 0
print(tpl[0])
print(tpl[3])
print(tpl[-2])

#slicing
tpl=(40,50,40,'xyz')
print(tpl[1:2])
print(tpl[1:])
print(tpl[-3:-1])

#change the tuple values
x=('python','data science','sql')
print(x)
y=list(x)
print(y)
#if we want to change the tuple means want to add any element then convert tuple into list and add element and again change that list to tuple
y[1]='big data'
print(y)
x=tuple(y)
print(x)

#tuple methods
#index()
t1=(1,2,'python',1,4,5,6)
print(t1.index('python'))

#count()
print(t1.count(1))

#nested tuple
tpl=('python',(1,2,3),('xyz'),('a'))
print(tpl[1][2])
print(tpl[2][2])

#tuple concatenation
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
t3=t1+t2
print(t3)
print(t1+(4,5,6))
print((1,2,3)+(4,5,6))

#tuple membership test='in' or 'not in'
tpl=('hi','1',2,'hello')
print(1 in tpl)
print('hi in tpl')
print('2' not in tpl)

#tuple constructor
mytuple=tuple(('hi','hello','hey'))
print(mytuple)

