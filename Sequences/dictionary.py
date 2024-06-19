#A Dictionary is a collection which is oredered and mutabe
#written using{}
#it stores key, value pairs

d1={1:'John',2:'bob',3:'bill'}
print(d1)
print(type(d1))

mydict={
        'brand':'bmw',
         'model':'3series',
         'year': 2019
}
print(mydict)

#Access dict items
print(mydict.items())
print(mydict['brand'])

#change the dict value
#change yr to 2020
mydict['year']=2020
print(mydict)

#add items to dict
mydict['color']='red'
print(mydict)

#remove dict items
#pop
mydict.pop('model')
print(mydict)

mydict.popitem()#will remove last item
print(mydict)

del mydict['year']
print(mydict)

#clear
mydict.clear()
print(mydict)

#copy dict-copy(),dict()
d2=mydict.copy()
print(d2)
d2=dict(mydict)

#join dicts
d1={1:10}
d2={2:20,3:30}
d1.update(d2)
print(d1)

#nested dict
d1={'key1':'123','key2':'value2','key3':{'inside':[1,2,'hell']}}
print(d1['key1'])
print(d1['key2'])
print(d1['key3'])
print(d1['key3']['inside'][2])
print(d1['key3']['inside'][2][1])
print(d1['key3']['inside'][2][1].upper())

#dict constructor-dict()
d1=dict(make='fork',model='ikon',year=2020)
print(d1)



