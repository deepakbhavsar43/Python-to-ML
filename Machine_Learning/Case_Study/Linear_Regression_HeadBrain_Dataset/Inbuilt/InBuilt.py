import pandas as pd
import numpy as np
import pickle
from userInput import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class HeadBrain:

    def load_data(self):
        dataset = pd.read_csv("Dataset/HeadBrain.csv")
        X = dataset["Head Size(cm^3)"]
        Y = dataset["Brain Weight(grams)"]
        return X, Y

    def Model(self, X, Y):
        dataset_length = len(X)
        X = X.values.reshape((-1, 1))
        reg = LinearRegression()
        reg = reg.fit(X, Y)
        return reg
        #, X

    def predict(self, reg, X):
        y_pred = reg.predict(X)
        return y_pred

    def score(self, reg, X, Y):
        r2 = reg.score(X, Y)
        print("R2 Score : ", r2)

    def plot_graph(self, reg, X, Y):
        max_x = np.max(X)
        min_x = np.min(X)

        x = np.linspace(min_x, max_x)
        y = reg.coef_ * x + reg.intercept_
        plt.plot(x, y, color="#ef5423", label="Regression")
        plt.scatter(X, Y, label="Scatter Plot")
        plt.xlabel("Head Size(cm^3)")
        plt.ylabel("Brain Weight(grams)")
        plt.legend()
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
    obj1 = HeadBrain()
    x, y = obj1.load_data()
    if args.train:
        reg_model = obj1.Model(x, y)
        obj1.wr_pickle(reg_model, Trained_Model_File)
        print("Model Trained")
    elif args.test:
        Trained_model = obj1.rd_pickle(Trained_Model_File)
        x=x.values.reshape((-1, 1))
        y_predict = obj1.predict(Trained_model, x)
        obj1.score(Trained_model, x, y)
        obj1.plot_graph(Trained_model, x, y)
