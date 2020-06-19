import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def assignment1(df, centroids, colmap):
    for i in centroids.keys():
        df[f'distance_from_{i}'] = (
            np.sqrt(
                (df['X'] - centroids[i][0]) ** 2 + (df['Y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['X'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['Y'])
    return k


df = pd.DataFrame({
    'X': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
    'Y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})

k = 3

centroids ={}
for i in range(k):
    centroids[i+1] = [np.random.randint(0, 80), np.random.randint(0, 80)]

colmap = {1: 'red', 2: 'green', 3: 'blue'}

# To visualize data-points and initial centroids
# plt.scatter(df["X"], df["Y"])
# for i in centroids.keys():
#     plt.scatter(*centroids[i], marker='x')
# plt.xlim(0, 80)
# plt.ylim(0, 80)
# plt.show()

co = 5
while co>0:
    df = assignment1(df, centroids, colmap)
    centroids = update(centroids)
    co-=1
print(df)
x, y = [], []
for i in centroids.keys():
    x.append(centroids[i][0])
    y.append(centroids[i][1])

plt.title('Custom')
plt.plot()
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(df['X'], df['Y'], c=df['closest'], label='Datapoints')
# for i in centroids.keys():
#     plt.scatter(centroids[i][0], centroids[i][1], marker='x', label="Centroids", c='blue')
plt.scatter(x, y, marker='x', label="Centroids", c='blue')

plt.xlim(0, 80)
plt.ylim(0, 80)
plt.legend()
plt.show()