# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

dict = {}

for i in range(4):
    key = input("Enter your name: ")
    value = input("Enter your favorite language: ")
    dict.update({key: value})

print(dict)