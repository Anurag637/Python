# Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  

n = int(input("Enter the number of rows for the star pattern:"))
space = " "
star = "*" * n
for i in range(1, n+1):
    if i == 1 or i == n:
        print(star)
    else:
        print("*" +space *(n-2) + "*")

'''
for n = 3
***
* *
***

'''
n = int(input("Enter no. of rows"))

for i in range(1,n+1):
    if i == 1 or i == n:
        print("*"*n)
    else:
        
        print("*" + " "*(n-2) + "*")
    