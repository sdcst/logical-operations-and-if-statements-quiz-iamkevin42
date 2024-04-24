"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math 


a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

c = int(input("Was A or B a hypotenuse\n"))

if a == c:
    d = print(a = c ** 2 - b**2)
    mathsqrtd = math.sqrt(d)
    e= round(d,1)
