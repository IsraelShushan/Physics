# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:43:05 2024

@author: ISRAELS4
"""

import numpy as np


## input
x1=float(input('enter x coordinate of the first vector: '))
y1=float(input('enter y coordinate of the first vector: '))
x2=float(input('enter x coordinate of the second vector: '))
y2=float(input('enter y coordinate of the second vector: '))

qn=int(input('enter question number to answer: '))
## your code

#---functions---

def angle_between_vectors(vector1,vector2): # calculate the angle between two vectors
    #calculate the product of two vectors
    dot_product = np.dot(vector1, vector2)
    # now calculate the norm of the two vector and the product of them
    norm_product = np.linalg.norm(vector1)*np.linalg.norm(vector2)
    cos_teta = dot_product/norm_product 
    teta_rad = np.arccos(np.clip(cos_teta, -1.0, 1.0))  # To handle floating-point precision issues
    # convert it to the radian using arccos
    teta_deg = np.degrees( teta_rad )
    return teta_deg

def calcualte_area_parallelogram(vector1,vector2): # calculate the area of a parallelogram by given two vectors
    # Calculate the cross product
    cross_product = np.cross(vector1, vector2)

    # Find the magnitude of the cross product
    area = np.linalg.norm(cross_product)
    return area

def is_rectangle(vector1,vector2): # by given two vectors return 1 if rectangle else 0  
    tetha = angle_between_vectors(vector1,vector2) #calculate the angle betwen two vectors
    norm1 = np.linalg.norm(vector1) 
    # calcualte the norm of the vectors
    norm2 = np.linalg.norm(vector2)
    # if the angle betwen two vector is 90 and the norm of the is difrrent is a rectangle else it a squeare or a parralelogram
    if(np.isclose(np.cos(np.radians(tetha)) ,0) and np.isclose(norm1, norm2)): # using the no.iscolse to due to potential floating-point precision issues
        return 1
    else:
        return 0
        
    
    
#--end funcitons --

# ---main code---

# create the verctor using numpy library
v1 = np.array([x1 , y1])
v2 = np.array([x2 , y2])
# y-axis reffernce vector
vector_y = np.array([0 , 1])

# create the add addition_vector
addition_vector = v1 + v2 
# create the subtraction
subtraction_vector = v1 - v2
#calculate alpha
alpha = angle_between_vectors(vector_y,subtraction_vector)
# calculate the area of the parallelogram
S= calcualte_area_parallelogram(v1,v2)
# determien if the two vector parallelogram is a rectangle
rect = is_rectangle(v1,v2)


# ---display graph code---



# ---end display graph code---

# ---end main---

## output
if qn==1:
    print(f'{alpha:.5g} degrees')
if qn==2:
    print(f'{S:.5g} squared meters')
if qn==3:
    print(rect)