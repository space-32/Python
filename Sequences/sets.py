#set is a collection which is unordered and unindexed
#written in {}
#it is mutable
#contains only unique elements
#Dosen't allow repetition of elements


s=set()
print(s)
print(type(s))

s={10,20,30,'Python',10,20}
print(s)
#in output there will be only one time 10 & 20 even though in set it is 2 times, since sets does not allow repetition
#order of the o/p keeps on changing, therefore it is unordered



#add elements to the set
#add()
s.add(40)
print(s)

#update()-for adding multiple elemnents
#for adding multiple elements use []
s.update([50,60,70,80])
print(s)

#remove items from set
s.remove(50)
print(s)
#if we try to remove element i.e. not there in set, remove will give keyerror
#but if we use discard for the element which is not in set, it'll print the set as it is
s.discard(30)
print(s)

#pop()
s1={'abc','xyz','pqr'}
print(s1)
s1.pop()
print(s1)

#join 2 sets
s1={1,2,3}
s2={4,5,6}
s3=s1.union(s2)
print(s3)
s1.update(s2)
print(s1)

#copy set-copy() and set()
s1={1,2,3}
print(s1)
s2=s1.copy()
print(s2)
s2=set(s1)
print(s2)

#difference of sets
x={'apple','fb','insta'}
y={'android','google','fb'}
z=x.difference(y) #x-y
print(z)
z=y.difference(x)
print(z)

#issubset()
x={'f','d','e','c','b','b'}
y={'a','b','c'}
z=y.issubset(x)
print(z)

x={'f','d','e','c','b','a'}
y={'a','b','c'}
z=y.issubset(x)
print(z)

#issuperset()
x={'f','d','e','c','b','a'}
y={'a','b','c'}
z=x.issuperset(y)
print(z)

#intersection()
s1={1,2,3,'1'}
s2={1,2,'1','1',1}
s3=s1.intersection(s2) #returns common elements
print(s3)


#set constructor
myset=set(('rose','jasmin','lily'))
print(myset)

#frozenset()
#when set is converted into frozen set then update, remove and clear cannot be performed

s={1,2,3}
print(s)
print(type(s))

f=frozenset(s)
print(f)
print(type(f))








