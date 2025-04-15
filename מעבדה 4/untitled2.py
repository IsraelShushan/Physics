import numpy as np


def zero_cross_eric(ar):
    H1t = np.sign(ar)
    H1s = np.abs(H1t[:-1] - H1t[1:])
    return np.nonzero(H1s)[0]


def main():
    m_in_km = 1000
    r_satelight = 6400*m_in_km
    r_earth = 30000*m_in_km
    T1 = 14*3600
    T2 = 24*3600
    t = np.linspace(0, 72*3600, 1000)
    
    #user input
    qn = int(input("Enter question number: "))
    n = int(input("Enter integer number: "))
    
    #calculations
    omega_satelight = t * (2*np.pi / T1)
    
    omega_earth = t * (2*np.pi / T2)
    
    #satelight location vector
    sate_light_x = r_satelight * np.cos(omega_satelight)
    sate_light_y = r_satelight * np.sin(omega_satelight)
    
    #earth location vector
    earth_x = r_earth * np.cos(omega_earth)
    earth_y = r_earth * np.sin(omega_earth)
    
    if (qn == 1):
        print(sate_light_x[n], sate_light_y[n])
        
main()
        

    
    
    
    
    
    