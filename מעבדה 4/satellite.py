import numpy as np


def zero_cross(ar):
    H1t = np.sign(ar)
    H1s = np.abs(H1t[:-1] - H1t[1:])
    return np.nonzero(H1s)[0]


R_earth = 6400
R_orbit = 30000
T = 14 * 3600
Day = 24 * 3600

time = np.linspace(0, 72 * 3600, 1000)

omega1 = 2 * np.pi / T
x_satellite = R_orbit * np.cos(omega1 * time) * 1000
y_satellite = R_orbit * np.sin(omega1 * time) * 1000

omega2 = 2 * np.pi / Day
x_nairobi = R_earth * np.cos(omega2 * time) * 1000
y_nairobi = R_earth * np.sin(omega2 * time) * 1000

distance = np.sqrt((x_satellite - x_nairobi)**2 + (y_satellite - y_nairobi)**2)
min_dot = np.gradient(distance)

zero_dot = zero_cross(min_dot)[1]
BMN = time[zero_dot] / 3600

n = int(input())
sn = int(input())

if sn == 1:
    print(x_satellite[n], y_satellite[n])
elif sn == 2:
    print(x_nairobi[n], y_nairobi[n])
elif sn == 3:
    print(BMN)
elif sn == 4:
    time = np.linspace(0, 72 * 4 * 3600, 1000)
    omega1 = 2 * np.pi / (21.6 * 3600)
    x_satellite = R_orbit * np.cos(omega1 * time) * 1000
    y_satellite = R_orbit * np.sin(omega1 * time) * 1000
    omega2 = 2 * np.pi / Day
    x_nairobi = R_earth * np.cos(omega2 * time) * 1000
    y_nairobi = R_earth * np.sin(omega2 * time) * 1000
    distance = np.sqrt((x_satellite - x_nairobi)**2 + (y_satellite - y_nairobi)**2)
    min_dot = np.gradient(distance)
    zero_dot = zero_cross(min_dot)[1]
    BMN2 = time[zero_dot] / 3600
    print(BMN2)