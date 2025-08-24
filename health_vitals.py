import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

full_health_data = pd.read_csv("full_data.csv", header=0, sep=",")
correlation_full_health = full_health_data.corr()
axis_corr = sns.heatmap(
    correlation_full_health,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(50, 500, n=500),
    square=True
)
plt.show()

# print(full_health_data["Duration"])    #this returns the data type of each variable
# print(full_health_data.describe())    #this can be use to summarize the data; returning info like variable count, mean, std, percentiles etc
# print(full_health_data.head())  #in case of a large dataset, this returns the first 5 rows 