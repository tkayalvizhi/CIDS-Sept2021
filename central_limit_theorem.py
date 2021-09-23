import numpy as np
import matplotlib.pyplot as plt


dataset_size = 100
num_of_datasets = 500
error_mean = 0
error_sd = 5


x_axis = np.linspace(0, 10, dataset_size)
y_actual = (2 * x_axis) + 3
plt.plot(x_axis, y_actual, 'r')

slope = 0
intercept = 0

for i in range(num_of_datasets):
    y = (2 * x_axis) + 3 + np.random.normal(error_mean, error_sd)
    m, b = np.polyfit(x_axis, y, 1)
    plt.plot(x_axis, m * x_axis + b, 'b', alpha=0.25)
    slope += m
    intercept += b

ave_slope = slope/num_of_datasets
ave_intercept = intercept/num_of_datasets
plt.plot(x_axis, ave_slope * x_axis + ave_intercept, color="green", linewidth=3, linestyle='dashed')

print(ave_slope, ave_intercept)

plt.show()