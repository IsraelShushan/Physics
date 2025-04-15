import numpy as np

# input
qn=int(input("Enter question number:"))

# your code goes here:
A = np.arange(0, 10, 1,dtype=np.float64)
B=np.power(10,A)-1
C=B[1:]-B[:-1]
D=C[::-1]
E=np.cumsum(D)
x = np.arange(0, 2 * np.pi, 0.01,dtype=np.float64)
f = np.power(np.sin(x), 2)
area_array=(f*0.01)
I = area_array.sum()  # Corrected line
F=np.cumsum(area_array)


#output section
if (qn==1):
    print(A)
elif (qn==2):
    print(B)
elif (qn==3):
    print(C)
elif (qn==4):
    print(D)
elif (qn==5):
    print(E)
elif qn==6:
    print(f)
elif qn==7:
    print(I)
elif qn==8:
    print(F)
'''# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:25:25 2024

@author: ISRAELS4
"""

import numpy as np

# input
qn=int(input("Enter question number:"))
# your code goes here:
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
A = np.arange(0,10 )
A_double = A.astype(np.float64)
#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Define the length of the series
length_of_series = 10

# Generate the series using a mathematical approach
series = [9*(10**i - 1) // 9 for i in range(length_of_series)]

# Convert to a NumPy array
array = np.array(series)

# Convert to double precision
B = array.astype(np.float64)
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C = np.diff(B)
#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
D = np.flip(C)
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
E = np.cumsum(D)
#ffffffffffffffffffffffffffffffffffffffffffff
array = np.arange(0,2*np.pi, 0.01)
sin_val = np.sin(array)
f = sin_val**2
#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
# Calculate the integral using the trapezoidal rule
I = np.trapz(f, array)
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


#output section
if (qn==1):
    print(A)

elif (qn==2):
    print(B)
    
elif (qn==3):
    print(C)

elif (qn==4):
    print(D)
    
elif (qn==5):
    print(E)
    
elif qn==6:
    print(f)
    
elif qn==7:
    print(I)
    '''