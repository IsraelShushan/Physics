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