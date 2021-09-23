import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# populate dataframe with data from csv
file_path = "D:\SupportVectors\Resources\DataSets\dataset-1.csv"
df = pd.read_csv(file_path)

# scatter plot of x and y
plt.plot(df['x'], df['y'], 'o', alpha=0.5)

# print(df)
# slope and y intercept
m, b = np.polyfit(df['x'], df['y'], 1)

# plot least square line
plt.plot(df['x'], m * df['x'] + b, 'r')
plt.show()