# Write a program to find whether a given number is prime or not. 

n = int(input("Enter a number: "))
if n <= 1:
    print("not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    print(f"{n} is prime")


num = int(input("Enter no. "))
if num <= 1:
    print("1 is not a prime no")
else:
    for i in range(num):
        if num % 2 == 0:
            print(f"{num} is not prine no. ")
            break
    else:
        print(f"{num} is prime no" ) 