# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:14:28 2024

@author: ISRAELS4
"""

#1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the GCD
print(gcd(num1, num2))


#2
import numpy as np

def create_series_and_sum(first, last, step):
    # Create the series
    series = np.arange(first, last , step, dtype=float)  # Include last element in the series

    # Print the series
    print(series)

    # Calculate and print the sum of the series
    series_sum = np.sum(series)
    print(series_sum)
# Input from the user
first_member = float(input("Enter the first member of the series: "))
last_member = float(input("Enter the last member of the series: "))
interval_size = float(input("Enter the interval size: "))

# Generate and print series and its sum
create_series_and_sum(first_member, last_member, interval_size)

#3
import numpy as np

def calculate_angle(vector_x, vector_y, vector_z):
    vector = np.array([vector_x, vector_y, vector_z])
    projection_xy = np.array([vector_x, vector_y, 0])

    dot_product = np.dot(vector, projection_xy)
    norms_product = np.linalg.norm(vector) * np.linalg.norm(projection_xy)
    cosine_angle = dot_product / norms_product
    angle_radians = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    angle_degrees = np.degrees(angle_radians)

    return angle_degrees

# User input for vector components
component_x = float(input("Component X: "))
component_y = float(input("Component Y: "))
component_z = float(input("Component Z: "))

# Calculating and printing the angle
calculated_angle = calculate_angle(component_x, component_y, component_z)

print(f'{calculated_angle:.5g}')

#4
import numpy as np

Ax=float(input("Ax: "))
Ay=float(input("Ay: "))
Az=float(input("Az: "))
B=np.array([3,4,-2])
## your code:
vector=np.array([Ax,Ay,Az])

dot_product=np.dot(vector, B)
norm_product=np.linalg.norm(vector)*np.linalg.norm(B)
cos_tetha = dot_product/norm_product
tetha_rad = np.arccos(np.clip(cos_tetha, -1.0, 1.0))  # To handle floating-point precision issues
alpha = np.degrees( tetha_rad )
##
print(alpha)

