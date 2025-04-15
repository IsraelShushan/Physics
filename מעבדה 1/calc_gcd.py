# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:29:46 2024

@author: ISRAELS4
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the GCD
print("The Greatest Common Divisor of", num1, "and", num2, "is:", gcd(num1, num2))
