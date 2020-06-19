import pickle
from userInput import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataframe import DataFrame
from sklearn.model_selection import train_test_split


class LogisticRegression:

    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        nSamples, nFeatures = X.shape

        # init parameters
        self.weights = np.zeros(nFeatures)
        self.bias = 0

        # gradient descent
        for _ in range(self.n_iters):
            # approximate y with linear combination of weights and x, plus bias
            linear_model = np.dot(X, self.weights) + self.bias
            # apply sigmoid function
            y_predicted = self._sigmoid(linear_model)

            # compute gradients
            dw = (1 / nSamples) * np.dot(X.T, (y_predicted - y))
            db = (1 / nSamples) * np.sum(y_predicted - y)
            # update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
        return linear_model

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_model)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        # print(y_predicted_cls)
        return np.array(y_predicted_cls)

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def accuracy(self, y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    def plot_graph(self):
        # X = X.to_numpy()
        # y =y.to_numpy()
        n_data, n_feature = X.shape
        plt.scatter(np.tile(y, n_feature), X)
        plt.show()

    def wr_pickle(self, train, model):
        # creating pickle file
        outfile = open(model, 'wb')
        # saving trained model in pickle file
        pickle.dump(train, outfile)
        outfile.close()

    def rd_pickle(self, model):
        # opening pickle file
        infile = open(model, 'rb')
        # loading the saved model into variable newTraining
        self.newTraining = pickle.load(infile)
        return self.newTraining


if __name__ == "__main__":
    Trained_Model_File = "Trained_Model/trained_data"
    data = pd.read_csv("Dataset/Titanic_Dataset.csv")
    data.drop("Embarked", axis=1, inplace=True)
    X = data.drop("Survived", axis=1)
    y = data["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
    regressor = LogisticRegression()
    model = regressor.fit(X_train, y_train)
    # print(type(model))
    regressor.wr_pickle(model, Trained_Model_File)
    model = regressor.rd_pickle(Trained_Model_File)
    # print(type(model))
    predictions = regressor.predict(X_test)
    print("Accuracy:", regressor.accuracy(y_test, predictions))
    regressor.plot_graph()
