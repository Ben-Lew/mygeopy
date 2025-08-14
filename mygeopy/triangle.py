import numpy as np

def hypot(a: float | np.ndarray,b: float | np.ndarray)-> float | np.ndarray:
    '''
    to calculate the hypotenus of a triangle
    a: float or array
    b: float or array
    
    RETURN
    float or array 
    '''
    return (a **2 + b**2)**0.5
