from csv import reader
from math import sqrt
import pandas as pd
from sklearn.metrics import accuracy_score


# Load a CSV file
def load_csv(filename):
    dataset = list()
    new_dataset = []
    new_label = []
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    dataset = dataset[1:]
    for row in dataset:
        new_dataset.append(row[0:4])
        new_label.append(row[-1])
    new_label = pd.factorize(new_label)[0]
    for i in range(0, len(dataset)):
        dataset[i][-1] = new_label[i]
    return dataset


# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


def accuracy(orignal_label, predicted_label):
    acc = accuracy_score(orignal_label, predicted_label, sample_weight=None)
    print("\nAccuracy :\n", acc * 100)


# Make a prediction with KNN on Iris Dataset
filename = 'iris-flower-dataset/IRIS.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0]) - 1):
    str_column_to_float(dataset, i)

# define model parameter
num_neighbors = 5
# define a new record
test_data = [[5.9, 3, 5.1, 1.8, 2],
             [5.7, 2.8, 4.1, 1.3, 1],
             [5, 3.3, 1.4, 0.2, 0]]

# predict the label
predict_lbl, ori_lbl = [], []
for row in test_data:
    label = predict_classification(dataset, row, num_neighbors)
    print('Data=%s, Predicted label: %s, Original label: %s' % (row[0:4], label, row[-1]))
    predict_lbl.append(label)
    ori_lbl.append(row[-1])
accuracy(ori_lbl, predict_lbl)