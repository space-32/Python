#Naming a module- we can name module anything we want and saved with .py extension

#Renaming a module- we can rename a module by giving it an alias name using 'as' keyword

import calc as ca
print(ca.add(2,3)) #here if we use as calc.add then it will give an error since now we renamed calc as ca so use ca
print(ca.sub(4,5))

#Choose to import specific part from module

from calc import add,person
print(add(2,3))
#no need to write the calc here bcz we've already imported the specific fxn from calc
print(person['city'])