import numpy as np

#inputs
m1=float(input())
m2=float(input())
F0=float(input())
v0=float(input())
qn=int(input())


###############
#your solution#
###############


F1 = -F0

a1x = F1 / m1

a2x = F0 / m2

#calc the time line
t_end = v0 / (-a1x+a2x)
t = np.linspace(0, t_end, 1000)
delta_t = t[1]-t[0]

#constant acceleration
v2x = 0 + (a2x * t)

p2 = m2 * v2x

#constant acceleration
v1x = v0 + (a1x * t)

p1 = m1 * v1x

P = p1+p2

##############################
EK1 = (0.5 *m1) * np.square(v1x)
EK2 = (0.5 *m2) * np.square(v2x)
EK = EK1 + EK2


#######
#output
if qn==1:
    print(p1[9])
elif qn==2:
    print(P[9])
