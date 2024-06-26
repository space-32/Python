#Function Arguments

def func(x):
    x=8
    print("X is:",x)


def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print("List is:",lst)
lst=[10,20,30]
update(lst)
#can also write above lst as update([10,20,30])


