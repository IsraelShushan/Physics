import numpy as np
import matplotlib.pyplot as plt

# set values for parameters
v0=7
m=0.1
b=0.3

# choose time step
dt=1e-3

# create index array
idx=np.arange(0,3000)
t=idx*dt # time array
v=np.zeros_like(t) #velocity arrary preparation
v[0]=v0 # set intial velocity

for i in idx:
	if i>0:
		v[i]=v[i-1]*(1-dt*b/m)

x=np.cumsum(v)*dt
v_th=v0*np.exp(-t*b/m)
x_th=m*v0/b*(1-np.exp(-b*t/m))

# plot the results
fig, (ax1,ax2)=plt.subplots(2,1)
ax1.plot(t,v,'o',label='numeric calculation')
ax1.plot(t,v_th,'--',label='analytic result')
ax1.set_ylabel('v (m/sec)')
ax1.legend(loc='upper right', shadow=True)
ax2.plot(t,x,'o',label='numeric calculation')
ax2.plot(t,x_th,'--',label='analytic result')
ax2.set_ylabel('x (m)')
ax2.set_xlabel('t (sec)')
ax2.legend(loc='lower right', shadow=True)