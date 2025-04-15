#imports and def
'''חישוב המהירות מתוך משדי"פ שהתקבלה(כתוצאה מכוח הגרר שתלוי בV) מהחוק השני של ניוטון. מתוך המהירות חישוב גם פונקציית המיקום'''
import numpy as np

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    sign_ar=np.sign(ar)
    sign_change_ar=np.abs(sign_ar[:-1]-sign_ar[1:])
    return np.nonzero(sign_change_ar)[0]

#input
sn=int(input())
v0=float(input())
m=float(input())
b=float(input())
g=9.8

#your code
dt = 1e-3
t = np.arange(0,3,dt)

#calc thev array
v = np.zeros_like(t)
v[0] = v0
for i in range(1,len(v)):
    v[i] = v[i-1]*(1-(b/m)*dt)-g*dt

#find the zeroing point
zeros_arr_v = zero_cross(v)
t1 = zeros_arr_v[0]*dt

#calc y function
#y = y0 + integral of v between 0-3
squers_of_integral_of_v = v * dt
integral_of_v = np.cumsum(squers_of_integral_of_v)
y = 0 + integral_of_v
#calc when the y func is zeroing at the second time
zeros_arr_y = zero_cross(y)
t2 = zeros_arr_y*dt - t1

#output
if sn==1:
    print(t1)
if sn==2:
    print(t2)