#Append to file

f=open('myfile.txt','a')
s=input("enter text:")
f.write('\n')
f.write(s)
f.close()