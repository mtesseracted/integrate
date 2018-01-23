"""
This file contains the implementation of the trapezoidal rule
"""

import numpy as np


def evaluate(x, f):
    a = x[0]
    b = x[1]
    ya = f(a)
    yb = f(b)
<<<<<<< HEAD
    I = (b - a) * (ya + yb) / 2.
=======
    I = (b - a) * (ya + yb) / 2
>>>>>>> 9bc509d72ead88d5ba43c6b2fafeb224779475a3
    return I
