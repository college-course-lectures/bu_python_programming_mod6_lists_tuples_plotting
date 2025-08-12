"""
Author: Professor Lewis
Date: August 11, 2025
Assignment: Module 1.3 Intro to Python
"""

"""
Program demonstrates input, processing, output,
converting strings to numeric values, the use of variables
and constants and formats using the f-string with Python
"""
print("Welcome to Python Programming!")

course_name = "Intro to Python"
print(f"You are enrolled in: {course_name}")

student_name = input("What is your name? ")
age = int(input("Enter your age: "))

CURRENT_YEAR = 2025
birth_year = CURRENT_YEAR - age

print(f"Hello, {student_name}! You were born in {birth_year}")

PI = 3.14159
radius =  float(input("Enter the radius of a circle: "))
area = PI * (radius ** 2)

print(f"The area of the circle is {area:.2f} square units.")

message = "Learning Python is" + " a valuable skill!"
print(message)

word1 = "Hello"
word2 = "World"

result = ",".join([word1, word2])
print(result)



