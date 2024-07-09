#Copy file
'''f=open('home.png','rb')
#rb bcz this is binary file, read binary(rb
f1= open('new_home.jpeg','wb')
for i in f:
    f1.write(i)'''

f=open('myfile.txt','r')
f1=open('newfile.txt','w')
for i in f:
    f1.write(i)
