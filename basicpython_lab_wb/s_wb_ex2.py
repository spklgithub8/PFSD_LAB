#1
#Program to display the factorial of a number:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input: Number
number = int(input("Enter a number: "))
# Output: Factorial
print(f"Factorial of {number}: {factorial(number)}")


#2
# Program to display the first 7 multiples of 7:
print("First 7 multiples of 7:")
for i in range(1, 8):
    print(7 * i)

#3
# Pythagorean Theorem
def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

# Input
side_a, side_b, side_c = map(float, input("Enter lengths of three sides separated by space: ").split())

# Output
print("It's a right triangle." if is_right_triangle(side_a, side_b, side_c) else "It's not a right triangle.")


#4
# Program for printing "*" according to the given input

n=int(input("Enter number of astriks you need:"))
x=1
for i in range (n):
        print("*"*x)
        x=x+1
x=n-1
for i in range (n):
        print("*"*x)
        x=x-1


#5
#binary comma seperated sequence
binary_sequence = input("Enter 4-binary digit numbers: ")
binary_numbers = binary_sequence.split(',')
divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]
print(','.join(divisible_by_5))

