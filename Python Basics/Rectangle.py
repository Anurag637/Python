'''
Print a rectangle with given number of rows and columns.

**********
*        *
*        *
**********

'''

r = int(input("Enter number of rows: "))    # 4
c = int(input("Enter number of columns: "))  # 10

for i in range(r):
    if i == 0 or i == r - 1:
        print("*" * c)
    else:
        print("*" + " " * (c - 2) + "*")


