import numpy as np
import matplotlib.pyplot as plt
import statistics


def get_cov_cor(x_array, y_array):
    """
    :param x_array: x parameter of a random variable
    :param y_array: y parameter of a random variable
    :return: covariance and correaltion of the two paramaters x and y
    """
    x_mean = statistics.mean(x_array)
    x_sd = statistics.stdev(x_array)
    y_mean = statistics.mean(y_array)
    y_sd = statistics.stdev(y_array)
    size = len(x_array)

    covariance = round(np.sum((x_array - x_mean) * (y_array - y_mean), axis=0) / size, 2)
    correlation = round(covariance/(x_sd * y_sd), 2)

    return (covariance, correlation)


def create_scatter_plot(x_a, y_a,  subplot):
    x_mean = statistics.mean(x_a)
    y_mean = statistics.mean(y_a)

    axes = subplot
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.spines['right'].set_color('None')
    axes.spines['top'].set_color('None')
    cov, cor = get_cov_cor(x_axis, y_a)
    subplot.title.set_text(f"cov = {cov} cor = {cor}")
    subplot.plot(x_a, y_a, 'o', alpha=0.75, markersize=2)
    subplot.plot(x_mean, y_mean, 'ro')
    subplot.grid(color='gray', alpha=0.25)


fig, ax = plt.subplots(2, 3)
x_axis = np.linspace(-10, 10, 100)

# First Plot: High positive correlation
y_axis = x_axis + np.random.normal(0, 1, 100)
create_scatter_plot(x_axis, y_axis, ax[0, 0])

# Second Plot: Medium positive correlation
y_axis = x_axis + np.random.normal(0, 5, 100)
create_scatter_plot(x_axis, y_axis, ax[0, 1])

# Third Plot: Low positive correlation
y_axis = x_axis + np.random.normal(0, 25, 100)
create_scatter_plot(x_axis, y_axis, ax[0, 2])

# fourth plot: Negative correlation
y_axis = (-1 * x_axis) + np.random.normal(0, 1, 100)
create_scatter_plot(x_axis, y_axis, ax[1, 0])

# fifth plot: 0 correlation symmetric function
y_axis = (100 - x_axis ** 2) ** 1 / 2
create_scatter_plot(x_axis, y_axis, ax[1, 1])

# sixth plot: completely random
y_axis = np.random.normal(0, 1, 100)
create_scatter_plot(x_axis, y_axis, ax[1, 2])

plt.show()
