'''Write a program to ditecd doube spaces in a String'''

# Ask the user to enter a string
a = input("Enter something: ")

# Check if there are double spaces in the string
if "  " in a:
    print("Double Space Detected")
else:
    print("No Double Space")
