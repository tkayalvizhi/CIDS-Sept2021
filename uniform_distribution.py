import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

import statistics
a = -10
b = 10
x = np.linspace(a, b, 100)
y = np.empty(100)
y.fill(1/(b-a))
print(1/(b-a))

plt.title("Uniform Distribution")
plt.plot(x, y, label="1/(b-a)")
plt.axvline(a, ymin=0, ymax=0.5, color='gray', linestyle='dashed')
plt.axvline(b, ymin=0, ymax=0.5, color='gray', linestyle='dashed')
plt.plot(a, 0.05, 'bo')
plt.plot(b, 0.05, 'bo')
plt.show()