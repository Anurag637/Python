#  Write a program to print multiplication table of n using for loops in reversed order. 

n = int(input("Enter the number for which you want to print the multiplication table: "))

# for i in range(10, 0, -1):
#     print(f"{n} X {i} = {n*i}")

i =10
while i>0:
    print(f"{n} X {i} = {n*i}")
    i =i-1


