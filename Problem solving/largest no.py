#create a program to find the largest number in a list using a for loop


# To take input from user
#n=list(map(int,input("Enter numbers seperated by spaces:").split))
#max_num=n[0]
n=[2,4,1,5,8,10]
max_num=n[0]
for i in n:
    if i>max_num:
        max_num=i
print(f"The largest number is in the list is:{max_num}")