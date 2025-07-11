# Write a recursive function to calculate the sum of first n natural numbers.

'''
1 = 1
2 = 1+2
2 = 1+2+3

n = 1+2+3+... + n-1+ n
'''
def sum_of_Natural_number(n):
    if n == 1:
        return 1
    return n + sum_of_Natural_number(n - 1)


result = sum_of_Natural_number(n = int(input("Enter a natural number: ")))
print("Sum:", result)
