# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 23:29:40 2024

@author: israe
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
## input
x1=float(input('enter x coordinate of the first vector: '))
y1=float(input('enter y coordinate of the first vector: '))
x2=float(input('enter x coordinate of the second vector: '))
y2=float(input('enter y coordinate of the second vector: '))
ids ='312423247'
# create the verctor using numpy library
v1 = np.array([x1 , y1])
v2 = np.array([x2 , y2])
# y-axis reffernce vector
vector_y = np.array([0 , 1])
# create the add addition_vector
addition_vector = v1 + v2 
# create the subtraction
subtraction_vector = v1-v2
fig, ax = plt.subplots() # create figure and ax lines
ax.set_xlim(0,10) # set limits to the a-axis and y-axis
ax.set_ylim(0,10)
ax.set_title('Vector Addition and Subtraction '+ids) # settitle
ax.set_xlabel('x(m)')
ax.set_ylabel('y(m)')
arrow_v1 = mpatches.FancyArrow(0, 0, v1[0] ,v1[1],linewidth=1 
,head_width=0.15,color='black') #create v1 arrow
arrow_v2 = mpatches.FancyArrow(0, 0,v2[0] ,v2[1],linewidth=1 
,head_width=0.15,color='black') # create v2 arrow
#create the addition arrow
arrow_addition_vector = mpatches.FancyArrow(0,0, addition_vector[0] 
,addition_vector[1],linewidth=1,head_width=0.15 ,color='red')
#create the subtraction_vector arrow
arrow_subtraction_vector = mpatches.FancyArrow(v2[0],v2[1],subtraction_vector[0],subtraction_vector[1],linewidth=1 
,head_width=0.15,color='green')
#arrow_v1_to_v2
arrow_v1_to_v2 = mpatches.FancyArrow(v1[0],v1[1],v2[0],v2[1],linewidth=1,head_width=0.15,color='black')
arrow_v2_to_v1 = mpatches.FancyArrow(v2[0],v2[1],v1[0],v1[1],linewidth=1,head_width=0.15,color='black')
ax.add_patch(arrow_v1)
ax.add_patch(arrow_v2)
ax.add_patch(arrow_addition_vector)
ax.add_patch(arrow_subtraction_vector)
ax.add_patch(arrow_v1_to_v2)
ax.add_patch(arrow_v2_to_v1)
plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

## input
x1=float(input('enter x coordinate of the first vector: '))
y1=float(input('enter y coordinate of the first vector: '))
x2=float(input('enter x coordinate of the second vector: '))
y2=float(input('enter y coordinate of the second vector: '))

qn=int(input('enter question number to answer: '))

## your code
vect1 = np.array([x1,y1])
vect2 = np.array([x2,y2])

res_sub = vect1 - vect2
res_add = vect1 + vect2

print(res_sub[0] )
print(res_sub[1])

fig, ax = plt.subplots()
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.grid(True)

ax.set_title('Vector Addition and Subtraction')
ax.set_xlabel('x')
ax.set_ylabel('y')

arw1=mpatches.Arrow(0, 0, x1, y1 ,width=0.2)
ax.add_patch(arw1)

arw2=mpatches.Arrow(0, 0, x2, y2 ,width=0.2)
ax.add_patch(arw2)

arw3=mpatches.Arrow(x2, y2, res_sub[0], res_sub[1] ,width=0.2, color='green')
ax.add_patch(arw3)

arw4=mpatches.Arrow(0, 0, res_add[0], res_add[1] ,width=0.2, color='red')
ax.add_patch(arw4)

arw5=mpatches.Arrow(x1,y1, x2, y2 ,width=0.2)
ax.add_patch(arw5)

arw6=mpatches.Arrow(x2, y2, x1,y12 ,width=0.2)
ax.add_patch(arw6)



plt.show()
'''






## output
'''
if qn==1:
    print(f'{alpha:.5g} degrees')
if qn==2:
    print(f'{S:.5g} squared meters')
if qn==3:
    print(rect)
'''