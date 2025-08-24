import sys
import matplotlib
# matplotlib.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

# health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line'),
# plt.ylim(ymin=0, ymax=400)
# plt.xlim(xmin=0, xmax=170)

# plt.savefig("plot.png")
# plt.show()
x = health_data['Average_Pulse']
y= health_data['Calorie_Burnage']

#********** Find Mean and Intercept using numpy.polyfit **************
# slope_intercept = np.polyfit(x, y, 1)
# print(slope_intercept)

# ******** PERCENTILES *************
percentile10 = np.percentile(y, 10)
print(percentile10)

#Two lines to make our compiler able to draw:
# sys.stdout.flush()
