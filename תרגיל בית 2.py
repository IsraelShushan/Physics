import numpy as np
import matplotlib.pyplot as plt


#to submit

ids = "312423247 318740834"

t=10
exponents = np.arange(2, 21, 1)  # Exponents from -2 to -20 with a step size of -1
delta_t = 1/10**exponents  # Create delta_t array using 10^-2, 10^-3, ..., 10^-20
actual_result=np.power(np.e,t)
center_deffrence=( np.power(np.e,t+delta_t)-np.power(np.e,t-delta_t) )/(2*delta_t)
absolute_error=np.abs(actual_result-center_deffrence)
graph=plt.plot(exponents,np.log(absolute_error),'-o')
plt.xticks(exponents, [f"{val}" for val in exponents], rotation=0, ha='right')


plt.xlabel("-log(Δt)")
plt.ylabel("log(Absolue Error)")
plt.title(ids)
plt.show()  # Corrected: Call plt.show() instead of plt.show


