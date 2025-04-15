import numpy as np

#this function returns the indexes where the function cross the zero axes. 
#in order to get the real value of the independet varible where the function cross the zero, you need to multiply that array with delta t
def zero_cross(y_vals):
    sign_arr = np.sign(y_vals)
    diff_arr = np.diff(sign_arr)
    zero_cross_indexes = np.nonzero(diff_arr)
    zero_indexes = zero_cross_indexes[0]    
    return zero_indexes
    
    '''מימוש אריק'''
def zero_cross_eric(ar):
    H1t = np.sign(ar)
    H1s = np.abs(H1t[:-1] - H1t[1:])
    return np.nonzero(H1s)[0]