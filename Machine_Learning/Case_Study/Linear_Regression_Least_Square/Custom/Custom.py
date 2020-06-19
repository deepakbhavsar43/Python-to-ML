import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
X = data["X"]
Y = data["Y"]
# print(f"{X} \n\n {Y}")

data_length = len(X)

# calculate mean of X and Y
xmean, ymean = 0, 0
for i in range(0, data_length):
    xmean += X[i]
    ymean += Y[i]
xmean = xmean / data_length
ymean = ymean / data_length

# calculate value of m
numerator, denominator = 0, 0
for i in range(0, data_length):
    numerator += (X[i] - xmean) * (Y[i] - ymean)
    denominator += (X[i] - xmean) ** 2
m = numerator / denominator

# Calculate C
c = ymean - m * xmean

YPerdicted = []
for i in range(0, data_length):
    temp = m * X[i] + c
    YPerdicted.append(temp)

top, down = 0, 0
for i in range(0, data_length):
    top += (YPerdicted[i] - ymean) ** 2
    down += (Y[i] - ymean) ** 2
r2Score = top/down
print(r2Score)


# Plot graph
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.scatter(X, Y, label="Scatter Plot")
plt.plot([X.min(), X.max()], [Y.min(), Y.max()], color="#ef5423", label="Regression Line")
plt.legend()
plt.show()