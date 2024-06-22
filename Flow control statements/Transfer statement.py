#Transfer statements are used to transfer control from one place to another inside the prog
#break,continue,pass
#break-breaks out the current enclosing loop
#continnue-goes to the top of current enclosing loop
#pass-does nothing at all

#break in for loop
mystr='Python'
for i in mystr:
    if i=='h':
        break
    print(i)

#break in while loop
x=0
while x<5:
    if x==3:
        break
    print(x)
    x+=1

#continue-will skip condition and continue with execution
#continue in for loop
mystring='django'
for i in mystring:
    if i=='a':
        continue
    print(i)
#in o/p a will be skipped from django

#continue in while loop
x=0
while x<25:
    x+=1
    if x%3==0:
        continue #skips multiples of 3
    print(x)
    #in while for continue, incrementation should be done before continue
    #x+=1

#pass-does nothing, simply will pass the control to next
x=[1,2,3]
for i in x:
    pass
print('end of script')

#for else
x=[10,11,12,15,20,25]
for i in x:
    if i%5==0:
        print(i)




