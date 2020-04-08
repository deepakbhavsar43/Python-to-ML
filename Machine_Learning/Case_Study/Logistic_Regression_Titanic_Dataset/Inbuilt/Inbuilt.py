from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from userInput import *
import pandas as pd
import pickle


class Dataset:

    def __init__(self):
        self.data = pd.read_csv("Dataset/Titanic_Dataset.csv")

    def read_dataset(self):
        self.data.drop("Embarked", axis=1, inplace=True)
        self.x = self.data.drop("Survived", axis=1)
        self.y = self.data["Survived"]
        return self.x, self.y

    def split(self, X, Y):
        # Splitting the data for training and testing
        self.xtrain, self.xtest, self.ytrain, self.ytest = train_test_split(x, y, test_size=0.3, random_state=0)
        return self.xtrain, self.xtest, self.ytrain, self.ytest

    def train(self, xTrain, yTrain):
        # Creating object of LogisticRegression model
        self.model = LogisticRegression()
        self.model.fit(self.xtrain, self.ytrain)
        return self.model

    def predict_label(self, model):
        # predicting y label
        self.yprediction = model.predict(self.xtest)
        print("\nInput given to model :\n", self.xtest)
        print("\nPredicted label by the model :\n", self.yprediction)

    def score(self, ytest):
        # Calculate accuracy of the model
        acc = accuracy_score(self.yprediction, ytest)
        print("Accuracy : ", acc * 100)

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
    obj = Dataset()
    x, y = obj.read_dataset()
    xtrain, xtest, ytrain, ytest = obj.split(x, y)
    if args.train:
        model = obj.train(xtrain, ytrain)
        obj.wr_pickle(model, Trained_Model_File)
        print("Model Trained")
    elif args.test:
        trained = obj.rd_pickle(Trained_Model_File)
        obj.predict_label(trained)
        obj.score(ytest)
