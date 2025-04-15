import numpy as np

def calculate_angle_between_vectors(vect1, vect2):
    dot_product = np.dot(vect1, vect2)
    norm_product = np.linalg.norm(vect1) * np.linalg.norm(vect2)
    cos_theta = dot_product / norm_product
    theta_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # To handle floating-point precision issues
    angle_degrees = np.degrees(theta_rad)
    return angle_degrees

# Inputs for the vector components
component_x = float(input("Enter X component of the vector: "))
component_y = float(input("Enter Y component of the vector: "))
component_z = float(input("Enter Z component of the vector: "))

# The second vector (you can replace these values with your specific vector)
second_vector = np.array([3, 4, -2])

# Creating the first vector from the input components
first_vector = np.array([component_x, component_y, component_z])

# Calculating the angle between the two vectors
angle = calculate_angle_between_vectors(first_vector, second_vector)
print(angle)