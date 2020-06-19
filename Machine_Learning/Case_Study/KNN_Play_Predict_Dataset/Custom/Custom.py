from math import sqrt
from csv import reader
import pandas as pd
from sklearn.metrics import accuracy_score


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
    # print("Predict method", type(dataset))
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


# Calculate accuracy
def accuracy(orignal_label, predicted_label):
    acc = accuracy_score(orignal_label, predicted_label, sample_weight=None)
    print("\nAccuracy :\n", acc * 100)


# Load a CSV file
def load_csv(filename):
    dataset = []
    with open("Dataset/Play_Predictor.csv", 'r') as file:
        csv_data = reader(file)
        for row in csv_data:
            # print(row)
            dataset.append(row[1:])
    dataset = dataset[1:]

    col1, col2, col3 = [], [], []
    row_length = len(dataset[0][1])
    for i in range(0, row_length):
        for row in dataset:
            col1.append(row[0])
            col2.append(row[1])
            col3.append(row[2])

    col1 = pd.factorize(col1)[0]
    col2 = pd.factorize(col2)[0]
    col3 = pd.factorize(col3)[0]
    # print(col1)

    row_length = len(dataset)
    # print(row_length)
    for i in range(0, row_length):
        dataset[i][0] = col1[i]
        dataset[i][1] = col2[i]
        dataset[i][2] = col3[i]
    return dataset


if __name__ == "__main__":

    # Make a prediction with KNN on Iris Dataset
    filename = 'iris-flower-dataset/IRIS.csv'
    dataset = load_csv(filename)
    # for i in range(len(dataset[0]) - 1):
    #     str_column_to_float(dataset, i)

    # define model parameter
    num_neighbors = 4

    # 38,Sunny,Cool,Yes
    # 39,Rainy,Mild,Yes
    # 40,Rainy,Cool,No

    # define test data
    test_data = [[0, 2, 1],
                 [2, 1, 1],
                 [2, 2, 0]]

    # predict the label
    predict_lbl, ori_lbl = [], []

    for row in test_data:
        label = predict_classification(dataset, row, num_neighbors)
        print('Data=%s, Predicted label: %s, Original label: %s' % (row[0:3], label, row[-1]))
        predict_lbl.append(label)
        ori_lbl.append(row[-1])

    # Display accuracy
    accuracy(ori_lbl, predict_lbl)
