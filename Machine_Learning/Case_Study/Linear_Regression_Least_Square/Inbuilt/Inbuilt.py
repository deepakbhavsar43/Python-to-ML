from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
X = np.array(X).reshape((-1,1))

linear_model = LinearRegression()
linear_model.fit(X, Y)
y_predict = linear_model.predict(X)
print(y_predict)
r2 = linear_model.score(X, Y)
print("Goodness of fit : ", r2)

plt.scatter(X, Y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.plot([X.min(), X.max()], [Y.min(), Y.max()])
plt.show()