from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris = pd.read_csv('Iris_Dataset/iris.csv')
iris = np.array(iris)
X = iris[:, :2]
y = iris[:, 4:5].reshape(1, -1)
# y = y.reshape(1, -1)
y = y[0]
print(y)
plt.title('Actual')
plt.scatter(X[:,0], X[:,1], c=y, cmap='gist_rainbow')
plt.xlabel('Spea1 Length')
plt.ylabel('Sepal Width')
plt.show()

km = KMeans(n_clusters = 3, n_jobs = 4, random_state=21)
km.fit(X)
centers = km.cluster_centers_
print(centers)

#this will tell us to which cluster does the data observations belong.
new_labels = km.labels_

# Plot the identified clusters and compare with the answers
plt.title('Predicted')
plt.scatter(X[:,0], X[:,1], c=new_labels, cmap='gist_rainbow')
plt.xlabel('Spea1 Length')
plt.ylabel('Sepal Width')
plt.show()

print(accuracy_score(y, new_labels))