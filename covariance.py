import numpy as np
import matplotlib.pyplot as plt

mean = 0
sd = 0.5
x_axis = np.linspace(-10, 10, 100)
print(x_axis)

y_axis = x_axis + np.random.normal(mean, sd, 100)
print(y_axis)