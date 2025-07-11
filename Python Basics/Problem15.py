# Write a program using functions to find greatest of three numbers. 

def greatest_No(num1, num2,num3):
    if num1 > num2 and num2 >num3:
        print(f"{num1} is greatest")
    elif num2 > num1 and num1 > num3:
        print(f"{num2} is greatest ")
    else:
        print(f"0{num3} is greatest") 

num1 = int(input("Enter 1st no. :"))
num2 = int(input("Enter 2nd no. :"))
num3 = int(input("Enter 3rd no. :"))

greatest_No(num1, num2,num3)