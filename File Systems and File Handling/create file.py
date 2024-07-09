#Create file using exclusive creation mode
#we can create the same name file using exclusive mode only once
#It means if i run the same program for 2nd time it will give me an error as file1 is already exist


f=open('file1','x') #we didn't mentioned extension so by default it willl create txt file
s=input('Enter some text:')
f.write(s)
f.close()