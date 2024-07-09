#Pickle load is deserilaze or unpickling

import pickle
#Here we only imported the pickle bcz student module is already imported in pickle_dump
f=open('student.dat','rb')
s=pickle.load(f)
s.show()
#display bcz in student def display is printing values
f.close()
