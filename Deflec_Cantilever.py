# Create a plot of simply-supported beam with one load

import matplotlib.pyplot as plt
import numpy as np

# import pandas as pd
# for testing:
# L = 10
# P = 50
# a = 2.5
# step = 1.15


def cantilever_deflection(L, P, a, step):

    b = L - a
    x = np.arange(0, L, step)  # create x-values for calcs
    if x[-1] < L:  # be sure that the last x-value = L
        x = np.append(x, L)
    print("x: ", x)
    print("Length of x is: ", len(x))
    print("X type is: ", type(x))
    # next three lines create deflection vector y based on formulas Left or Right of Load position, i.e. x<=a, and x>a
    deflec_x_less_a = -P * x**2 * (3 * a - x)
    deflec_x_more_a = -P * a**2 * (3 * x - a)
    y = np.where(x <= a, deflec_x_less_a, deflec_x_more_a)
    # y_flat = 0 * x
    print("y: ", y)
    print("length of y is ", len(y))
    print("Y type is: ", type(y))
    return x, y
