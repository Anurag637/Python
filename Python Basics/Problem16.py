# Write a python program using function to convert Celsius to Fahrenheit. 

def Temp_convertor1(Celsius_temp):
    Fahrenheit = Celsius_temp * 9/5 + 32
    print(Fahrenheit)
Celsius_temp = int(input("Enter temperture in Celsius: "))
Temp_convertor1(Celsius_temp)


def Temp_convertor2(Fahrenheit_temp):
    Celsius = (Fahrenheit_temp - 32 )*5/9
    print(Celsius)
Fahrenheit_temp = int(input("Enter temperture in Fahrenheit: "))
Temp_convertor2(Fahrenheit_temp) 