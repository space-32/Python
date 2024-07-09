#working with dir(directory)

import os
print(os.getcwd()) #current working directory

print(os.listdir())

#Create a new directory

#os.mkdir('mypics')  #make directory(dir)

#Rename the above dir
#os.rename('mypics','myimages')


#how to delete a dir or remove a dir
#os.rmdir('myimages')
print(os.getcwd())

#check dir
#It will be a boolean check
check_dir=os.path.isdir("/Users/pournimalanjekar/PycharmProjects/py practice/File Systems and File Handling")
print(check_dir)


