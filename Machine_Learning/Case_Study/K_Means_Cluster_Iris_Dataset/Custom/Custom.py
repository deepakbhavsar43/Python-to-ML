import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def min_max(data):
    xmin = min(data['sepal_length'])
    ymin = min(data['sepal_width'])
    xmax = max(data['sepal_length'])
    ymax = max(data['sepal_width'])
    return xmin, ymin, xmax, ymax


def assignment1(df, centroids):
    for i in centroids.keys():
        df[f'distance_from_{i}'] = (
            np.sqrt(
                (df['sepal_length'] - centroids[i][0]) ** 2 + (df['sepal_width'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df


def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['sepal_length'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['sepal_width'])
    return k


df = pd.read_csv('Iris_Dataset/iris.csv')
xmin, ymin, xmax, ymax = min_max(df)

k = 3
centroids = {
    i + 1: [np.random.randint(xmin, xmax), np.random.randint(ymin, ymax)] for i in range(k)
}

# plot initial data
plt.scatter(df["sepal_length"], df["sepal_width"])
colmap = {1: 'red', 2: 'green', 3: 'blue'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i], edgecolors='black')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.xlim(4, 8)
plt.ylim(1.5, 5)
plt.show()

iter = 50

while iter > 0:
    df = assignment1(df, centroids)
    centroids = update(centroids)

    iter -= 1

plt.scatter(df["sepal_length"], df["sepal_width"], color=df['color'])
colmap = {1: 'red', 2: 'green', 3: 'blue'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i], marker='x')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.xlim(4, 8)
plt.ylim(1.5, 5)
plt.show()
