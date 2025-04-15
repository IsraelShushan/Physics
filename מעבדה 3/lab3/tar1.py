import numpy as np

def zero_cross(y_vals):
    sign_arr = np.sign(y_vals)
    diff_arr = np.diff(sign_arr)
    zero_cross_indexes = np.nonzero(diff_arr)
    zero_indexes = zero_cross_indexes[0]
    
    return zero_indexes
    
    


# input 
v0=float(input("Enter v0:"))
# const
g=9.8 # m/s^2
t=np.arange(0,7,0.01)
y=-0.3+v0*t-0.5*g*t**2 #becomes an array

#print(y[zc])
##time_of_flight = diff
## your code
#solution one:
zc = zero_cross(y)
#solution two:
p = [-0.5*g, v0, -0.3]
root = np.roots(p)
time = abs(root[1]-root[0])







time_of_flight=(zc[1]-zc[0])*0.01

#output
print(f'time: {time:.5g} s')
print(f'time of flight: {time_of_flight:.5g} s')