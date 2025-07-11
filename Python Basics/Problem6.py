# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

dictionary = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "शुभकामनाएँ": "Best wishes",
    "सुप्रभात": "Good morning",
    "शुभ रात्रि": "Good night",
    "आप कैसे हैं?": "How are you?",
    "मुझे माफ करें": "Excuse me",
    "बिल्कुल": "Absolutely",
    "ठीक है": "Okay"
}
word = input("Enter a Hindi word to translate to English: ")

if word not in dictionary:
    print("Sorry, the word is not in the dictionary.")
else:
    print(dictionary[word])