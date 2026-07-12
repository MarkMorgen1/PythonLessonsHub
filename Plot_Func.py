# Plotting Graphs in Python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a plot of simply-supported beam with one load
L = 10.0
P = 500.0
a = 2.0
step = 0.05
b = L - a

x = np.arange(0, L, step)  # create x-values
print(x[-1])
print(len(x))
if x[-1] < L:
    x = np.append(x, L)
print("x: ", x)
print("Length of x is: ", len(x))
print(type(x))
# next three lines create deflection vector y based on formulas Left or Right of Load position, i.e. x<=a, and x>a
base_term = (-P * b * x / L) * (L**2 - b**2 - x**2)
load_correction = P * (x - a) ** 3
y = np.where(x <= a, base_term, base_term - load_correction)
y_flat = 0 * x
print("y: ", y)
print("length of y is ", len(y))


plt.plot(x, y)
plt.plot(x, y_flat)
plt.xlabel("X-values")
plt.ylabel("Y-values")
plt.title("Deflection Curve")
plt.show()
