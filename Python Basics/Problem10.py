# Write a program to find the greatest of four numbers entered by the user.

list = []
for i in range(4):
    num = int(input("Enter no: "))
    list.append(num)

print(f"Greatest no: {max(list)}")