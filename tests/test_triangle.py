import sys
import os
import numpy as np
from mygeopy.triangle import hypot

def test_hypot():
    assert hypot(3,4) == 5

def test_hypot_negative():
    assert hypot(-3.0,-4) == 5

def test_hypot_array():
    arr3,arr4 = np.ones(10)*3,np.ones(10)*4
    assert np.all(hypot(arr3,arr4) == np.ones(10)*5)

def test_hypot_inf():
    assert np.isinf(hypot(np.inf,1))

# def test_hypot_string():
#     assert hypot("a",1)
if __name__ == "__main__":
    import doctest
    doctest.testmod()