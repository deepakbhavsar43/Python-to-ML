# import necessary packages
import pickle
from userInput import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


class predict_lbl:

    # initialize path of the dataset file
    def __init__(self, path):
        self.path = path

    # read data from csv file
    def read_csv(self):
        self.iris = pd.read_csv(self.path)
        self.x = self.iris.drop(["species"], axis=1)
        self.y = self.iris["species"]

    # split the data for training and testing
    def split(self):
        xtrain, xtest, ytrain, ytest = train_test_split(self.x, self.y, test_size=0.2, random_state=0)
        return xtrain, xtest, ytrain, ytest

    # training the model
    def train(self,xtrain, ytrain, key = 6):
        print("key", key)
        knn = KNeighborsClassifier(n_neighbors = key)
        trained_model = knn.fit(xtrain, ytrain)
        return trained_model

    # saving the trained model into pickle file
    def wr_pickle(self, Trained_Model, pickle_File_path):
        with open(pickle_File_path, 'wb') as outfile:
            pickle.dump(Trained_Model, outfile)

    # reading the data from pickle file
    def rd_pickle(self, pickle_file_path):
        with open(pickle_file_path, 'rb') as infile:
            knn = pickle.load(infile)
            return knn

    # predict the label of test data
    def predict(self, knn, xtest):
        ylbl = knn.predict(xtest)
        print("\nGiven test data :\n", xtest)
        print("\nPredicted lable :\n", ylbl)
        return ylbl

    # check the accuracy of model
    def accuracy(self, orignal_label, predicted_label):
        acc = accuracy_score(orignal_label, predicted_label, sample_weight=None)
        print("\nAccuracy :\n", acc * 100)


if __name__ == "__main__":
    dataset_path = "iris-flower-dataset/iris.csv"
    pickle_file = "Trained_Model/trained_data"
    obj = predict_lbl(dataset_path)
    obj.read_csv()
    xtrain, xtest, ytrain, ytest = obj.split()

    if args.train:
        trained_model = obj.train(xtrain, ytrain)
        obj.wr_pickle(trained_model, pickle_file)
        print("Model Trained.")
    elif args.test:
        model = obj.rd_pickle(pickle_file)
        label = obj.predict(model, xtest)
        obj.accuracy(ytest, label)