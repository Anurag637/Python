# Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 

n = set()
for i in range(8):
    num = int(input("Enter  nos: "))
    n.add(num)

unique_numbers = set(n)
print(unique_numbers)