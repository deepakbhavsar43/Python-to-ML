import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.DataFrame({
    'X': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
    'Y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})
df = np.array(df)

# finding best value of K using elbow method
var = []
for i in range(1, 11):
    k_mean = KMeans(n_clusters=i, init='k-means++', random_state=42)
    k_mean.fit(df)
    var.append(k_mean.inertia_)
print(var)


# plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), var,marker='o',color='red')
plt.title('Elbow Point')
plt.xlabel('Number of clusters')
plt.ylabel('variation')
plt.show()

k_mean = KMeans(n_clusters=3)
k_mean.fit(df)

centroids = k_mean.cluster_centers_

print("\nCentroids : \n", centroids)
print("\nLabels : \n", k_mean.labels_)

plt.title('Inbuilt')
plt.plot()
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(df[:,0], df[:,1], c=k_mean.labels_, label='datapoints')
plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", label="Centroids")
plt.legend()
plt.show()