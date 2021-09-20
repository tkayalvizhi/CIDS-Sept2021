import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics


def plot_normal(sd):
    # Plot between -10 and 10 with .001 steps.
    x_axis = np.arange(-50, 50, 0.01)
    mean = statistics.mean(x_axis)
    plt.plot(x_axis, norm.pdf(x_axis, mean, sd))


plt.title("Normal Distribution")
plot_normal(10)
plot_normal(5)
plot_normal(20)
plt.legend(["σ²:100", "σ²:25", "σ²:400"], loc="upper right")
plt.show()