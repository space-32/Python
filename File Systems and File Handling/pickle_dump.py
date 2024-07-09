#Pickle dump is writing or dumping the file

import pickle,student
#student is name of module

f=open('student.dat','wb')
s=student.Student(11,'sam','95')
#Student is name of class

pickle.dump(s,f)
#s dump to f
f.close()

#if we run this code the file name student.dat will created which is in binary, so we are not able to read that
#so to read this file we need to read the data back which is in file pickle load
