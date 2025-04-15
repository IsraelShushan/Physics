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

arw3=mpatches.Arrow(x2, y2, res_sub[0], res_sub[1] ,width=0.2)
ax.add_patch(arw3)

arw4=mpatches.Arrow(0, 0, res_add[0], res_add[1] ,width=0.2)
ax.add_patch(arw4)

arw5=mpatches.Arrow(x1,y1, x2, y2 ,width=0.2)
ax.add_patch(arw5)

#arw6=mpatches.Arrow(x2, y2, res_add[0], res_add[1] ,width=0.2)
#ax.add_patch(arw6)



plt.show()






## output
'''
if qn==1:
    print(f'{alpha:.5g} degrees')
if qn==2:
    print(f'{S:.5g} squared meters')
if qn==3:
    print(rect)
'''