# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 
Name = input("Enter name of student: ")
Hindi = int(input("Enter marks of Hindi: "))
English = int(input("Enter marks of English: "))
Maths = int(input("Enter marks of Maths: "))
total_marks = Hindi + English + Maths


total_percentage = (total_marks /300) *100
hindi_percentage = (Hindi / 100) * 100
english_percentage = (English / 100) * 100  
maths_percentage = (Maths / 100) * 100
if(total_percentage >= 40):
    if(hindi_percentage >=33 and english_percentage >= 33 and maths_percentage >= 33):
        print(f"{Name} has passed with {total_percentage}%") 
    else: 
      print(f"{Name} has failed")
else: 
    print(f"{Name} has failed") 