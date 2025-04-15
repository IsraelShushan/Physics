import matplotlib.pyplot as plt
import numpy as np
import math

# Time array
t = np.linspace(0, 2, 500)  # 2 seconds, 500 points

# Parameters
amplitudes = [1, 2]
frequencies = [1, 2]

k= 20
m= 1
v0 = 0
x0 = 1
w0 = math.sqrt(k/m)

#for the linear kfitz
x = x0 * -np.cos(w0*t)+v0/w0 * np.sin(w0*t)

# Create figure and axes
fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# Generate plots
for i, A in enumerate(amplitudes):
    for j, f in enumerate(frequencies):
        x = A * np.sin(2 * np.pi * f * t)
        axs[i, j].plot(t, x)
        axs[i, j].set_title(f'Amplitude = {A}, Frequency = {f} Hz')
        axs[i, j].set_xlabel('Time (s)')
        axs[i, j].set_ylabel('x(t)')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()