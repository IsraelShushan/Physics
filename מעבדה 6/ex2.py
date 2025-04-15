# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:43:39 2024

@author: ISRAELS4
"""
import matplotlib.pyplot as plt
import numpy as np
import math

k=40
m=2
x0=float(input("initial position: "))
v0=float(input("initial velocity: "))

def Simple_HM_A1(x0,v0,dt,t_last):
    v = np.zeros(len(t))
    x = np.zeros(len(t))
    x[0] = x0
    v[0] = v0
    for i in range(1, len(t)):
        v[i] = v[i-1] - k/m * x[i-1]*dt
        x[i] = x[i-1] + v[i-1]*dt
    return t, x, v
     
def Simple_HM_A2(x0,v0,dt,t_last):
    v = np.zeros(len(t))
    x = np.zeros(len(t))
    x[0] = x0
    v[0] = v0
    for i in range(1, len(t)):
        v[i] = v[i-1] - k/m * x[i-1]*dt
        x[i] = x[i-1] + v[i]*dt
    return t, x, v
    
    
dt=0.01
t_last=10
t = np.arange(0,t_last,dt)







t,x_A1,v_A1=Simple_HM_A1(x0,v0,dt,t_last)
t,x_A2,v_A2=Simple_HM_A2(x0,v0,dt,t_last)

w0 = math.sqrt(k/m)

x_th= x0 * np.cos(w0*t)+v0/w0 * np.sin(w0*t)


D1=np.abs(x_th[300]-x_A1[300])
D2=np.abs(x_th[300]-x_A2[300])

#output
print(f'{x_A1[300]:.5g}')
print(f'{x_A2[300]:.5g}')
print(f'{D1:.5g}')
print(f'{D2:.5g}')

fig, axs = plt.subplots(1, 2, figsize=(10, 6))
axs[0].plot(t, x_A1)
axs[1].plot(t, x_A2)
axs[0].set_title("v(i)")
axs[1].set_title("v(i-1)")

axs[0].set_xlabel('x(t)')
axs[0].set_ylabel('t')
axs[1].set_xlabel('x(t)')
axs[1].set_ylabel('t')
plt.show()