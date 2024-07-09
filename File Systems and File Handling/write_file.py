#File is a space where we store and organize our data
#Data could be anything like text data, binary data(images,audio,video)


#Open a file
#open(file_name,mode)
#modes are w,r,a,x  i.e. write,read,append,exclusive respectively

#Close a file
#f.close()   f is considered as a name of file

#mode
'''
w- write to file
r - read from file
a - append to file
x - exclusive file creation mode
'''

#Binary files
#wb,rb,ab

#Write some string to a file
'''f=open('myfile.txt','w') #extension is by default txt
s=input("enter text:")
f.write(s)
f.close()'''

#below code allows to write multiple strings in file, above code is allowing only one string
f=open('myfile.txt','w')
print('Enter text:,(Type "#" when you are done)')
s=' '
while s!='#':  #we can specify any character we want
    s=input()#it will take any input from user since we are not mentioning it
    f.write('\n') #new line
    f.write(s)
f.close()

