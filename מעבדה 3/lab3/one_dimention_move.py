import numpy as np
from zero_cross import zero_cross
import matplotlib.pyplot as plt



#functions
def create_time_arr(delta_t):
    t = np.arange(0, 5, delta_t)
    return t

#declerations:
v0=float(input("vo: "))
gamma=float(input("gamma: "))
qn=int(input("q#:"))
delta_t = 0.01

#A
t = create_time_arr(delta_t)
#B
vx = v0*np.e**(-gamma*t)*np.cos(10*gamma*t)
#C
ax = np.gradient(vx)/delta_t
#D
x0 = 0
#array of mini squeres areas
vx_areas = vx * delta_t
#sum all the mini squares like Riman's sum
integral_of_vx = np.cumsum(vx_areas)
#x equation
x = x0 + integral_of_vx
#E
#find the roots of the x equation
#p = [a,b,c]
#root = np.roots(x)
#third_root = root[2]
#cannot be used because it isn't polinom
zero_indexes = zero_cross(vx)
#get the real time
third_zeroing = zero_indexes[2]*delta_t

#FOR HW3
ids = 318740834 
plt.plot(t,x)
plt.xlabel("Δt")
plt.ylabel("x(Δt)")
plt.title(ids)
plt.show()  # Corrected: Call plt.show() instead of plt.show






if qn==1: 
    print(t[:10])
elif qn==2: 
    print(vx[:10])
elif qn==3:
    print(ax[:10])
elif qn==4:
    print(x[:10])    
elif qn==5:
    print(third_zeroing)
