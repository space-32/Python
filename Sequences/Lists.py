#Lists are sequences/collection which are ordered
#Lists can store any numbers of elements
#Lists allows duplication
#Written using []

lst=[]
print(lst)
print(type(lst))

lst=[10,20,30,'Python',-10,30.5]
print(lst)

#Repetition
print(lst * 2)

#find the len of list
print(len(lst))

#indexing
print(lst[0])
print(lst[2])
print(lst[-2])

#Slicing
print(lst[0:4])#including 0 but excluding 4
print(lst[1:])
print(lst[-3:-1])
print(lst[1::2])#will start from 1 and will print all alternate
#print(lst[::-1])#will reverse the string

#List Methods
#Add and remove items from list
#append()
lst.append(40)#will add the element at end
print(lst)

#insert()-add element at the specified index
lst.insert(1,50)#1 is index and 50 is an element
print(lst)

#extend()-can add multiple elements
lst.extend([3,6,7])
print(lst)

#remove()
lst.remove('Python')
print(lst)


#pop(index)
lst.pop(1)#item from index 1 is removed i.e. 50
print(lst)

#pop()-will only remove the last element
lst.pop()
print(lst)

#del
del lst[6]
print(lst)

#max() and min()
print(max(lst))
print(min(lst))

#sort()
lst.sort()#ascending order
print(lst)

lst.sort(reverse=True)#descending order
print(lst)

#copy list using copy() and list()
l1=[1,2,3]
print(l1)
l2=l1.copy()
print(l2)

#List concatenation
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)

#Nested lists
lst=['hello',[1,2,3],['a']]#inex of hello is 0,[1,2,3] is 1 and ['a'] is 3
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[0][1])# if we want to print e from hello so the hello is at 0 index and characters also has indexing so for e inex is 1
#we can even print multiple characters from hello using slicing syntax inside that [1]
print(lst[1][1])
print(lst[2][0])

#List mebership test-'in' and 'not in'
lst=['hi','hello','1','bye''2']
print('hi'in lst)
print('1' not in lst)
print('1' and 'hi' in lst)
#if both are in list then only will return true bcz of and


#List constructor-list(())
mylist=list(('usa',"Uk",'India'))
print(mylist)

#index()
l=[1,23,4,5,6]
print(l.index(5))

#count()
print(l.count(23))

#Lists are mutable
lst=['usa','uk','India','china']
print(lst)
lst[1]='canada'#will change uk to canada
print(lst)
#lst[4]='Germany', here this will give an error bcz inexing is just to change the element not to add new element to add new element use append


