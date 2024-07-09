#Checking file
import os,sys
'''if os.path.isfile('myfile1.txt'):
    f=open('myfile.txt','r')
    s=f.read()
    print(s)
    f.close()
else:
    print("File does not exist")'''

check_file=os.path.isfile('myfile.txt')
print(check_file)
