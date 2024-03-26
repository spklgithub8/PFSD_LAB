#1
#caluclate an average in python

numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]
average = sum(numbers) / len(numbers)
print("Average:", average)

#2
"""Program to accept an integer value from a user in Python and to convert an 
input string value into an integer using an int () function."""

string_value = input("Enter a string value: ")
integer_value = int(string_value)
print("Converted integer value:", integer_value)


#3
#Program to add two complex, float, and integer numbers

complex_num1 = complex(input("Enter the first complex number: "))
complex_num2 = complex(input("Enter the second complex number: "))
float_num1, float_num2 = float(input("Enter a float number: ")), float(input("Enter another float number: "))
int_num1, int_num2 = int(input("Enter an integer: ")), int(input("Enter another integer: "))
print("Sum of complex numbers:", complex_num1 + complex_num2)
print("Sum of float numbers:", float_num1 + float_num2)
print("Sum of integers:", int_num1 + int_num2)


#4
#Program to convert integer to float

float_value = float(input("Enter an integer: "))
print("Converted float:", float_value)



#5
#Program to perform addition of string and integer using explicit conversion

string_value = input("Enter a string: ")
integer_value = int(input("Enter an integer: "))
result = int(string_value) + integer_value
print("Result of addition:", result)
