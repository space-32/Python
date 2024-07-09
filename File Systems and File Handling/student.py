#Pickle module is use to serialize the file

class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks

    def show(self):
           print(self.id,self.name,self.marks)

