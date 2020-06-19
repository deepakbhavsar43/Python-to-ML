import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from commands import userInput as uic


# Converted textual data into numbers manually
# 0 = Rough, Tennis
# 1 = Smooth, Cricket
# X = [[35, 0], [47, 0], [90, 1], [48, 0], [90, 1], [35, 0], [92, 1], [35, 0], [35, 0], [35, 0], [96, 1], [43, 0],
#      [110, 1], [35, 0], [95, 1]]
# y = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]

class Dataset:

    def __init__(self, file):
        self.dataset = pd.read_csv(file)

    def read_dataset(self):
        self.dataset["Species"] = pd.factorize(self.dataset.Species)[0]
        # self.dataset["Label"] = pd.factorize(self.dataset.Label)[0]
        self.X = self.dataset.drop(["Species"], axis=1)
        self.Y = self.dataset["Species"]
        return self.X, self.Y

    def split(self, X, Y):
        # Splitting the data for training and testing
        self.xTrain, self.xTest, self.yTrain, self.yTest = train_test_split(X, Y, test_size=0.2, random_state=0)
        return self.xTrain, self.xTest, self.yTrain, self.yTest

    def train(self, xTrain, yTrain):
        # Creating object of decision tree
        dtc = DecisionTreeClassifier()
        # Fitting the training data
        self.training = dtc.fit(xTrain, yTrain)
        return self.training

    def predict_label(self, model, xTest):
        # Dataset.rd_pickle()
        # predicting
        self.yPredict = model.predict(xTest)
        # Displaying the result
        p_lbl = []
        for lbl in self.yPredict:
            if lbl == 0:
                # print("Setosa")
                p_lbl.append("setosa")
            elif lbl == 1:
                # print("versicolor")
                p_lbl.append("versicolor")
            else:
                # print("virginica")
                p_lbl.append("virginica")
        return p_lbl

    def score(self, model, yTest):
        # Calculate accuracy of the model
        accuracy = (accuracy_score(yTest, self.yPredict, sample_weight=None) * 100)
        print("Decision Tree\nAccuracy on Iris dataset: ", accuracy)
        return accuracy

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
    CSVFileName = "Dataset/iris.csv"
    Trained_Model_File = "Trained_Model/Inbuilt/trained_data"
    obj = Dataset(CSVFileName)
    X, Y = obj.read_dataset()
    xTrain, xTest, yTrain, yTest = obj.split(X, Y)
    d_tree = 0

    if uic.args.train:
        # print(xTrain, yTrain)
        model = obj.train(xTrain, yTrain)
        obj.wr_pickle(model, Trained_Model_File)
        print("Model Trained")
    elif uic.args.test:
        trained = obj.rd_pickle(Trained_Model_File)
        # print(type(trained))
        obj.predict_label(trained, xTest)
        obj.score(trained, yTest)
    elif uic.args.predict:
        trained = obj.rd_pickle(Trained_Model_File)
        sl, sw, pl, pw = [], [], [], []
        sl.append(uic.args.sepallength)
        sw.append(uic.args.sepalwidth)
        pl.append(uic.args.petallength)
        pw.append(uic.args.petalwidth)
        to_predict = pd.DataFrame({
            "SepalLengthCm":sl,
            "SepalWidthCm":sw,
            "PetalLengthCm":pl,
            "PetalWidthCm":pw
        })
        # print(to_predict)
        trained = obj.rd_pickle(Trained_Model_File)
        lable = obj.predict_label(trained, to_predict)
        print("predicted species: ",lable[0])
