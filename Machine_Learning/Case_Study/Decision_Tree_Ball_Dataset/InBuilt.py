import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import userInput as uic


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
        self.dataset["Surface"] = pd.factorize(self.dataset.Surface)[0]
        self.dataset["Label"] = pd.factorize(self.dataset.Label)[0]
        self.X = self.dataset.drop(["Label"], axis=1)
        self.Y = self.dataset["Label"]
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

    def test(self, model, xTest):
         self.yPredict = model.predict(xTest)

    def predict_label(self, model, xTest):
        # predicting
        self.yPredict = model.predict(xTest)
        # Displaying the result
        # print("0 = Rough, Tennis\n1 = Smooth, Cricket")
        # print("\nInput given to model :\n", xTest)
        # print("\nPredicted label by the model :")
        for lbl in self.yPredict:
            if lbl == 0:
                print("Tennis")
            else:
                print("Cricket")

    def score(self, model, yTest):
        # Calculate accuracy of the model
        accuracy = accuracy_score(yTest, self.yPredict, sample_weight=None)
        print("Accuracy : ", accuracy * 100)
        return self.yPredict

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
    CSVFileName = "Dataset/Ball_Dataset.csv"
    Trained_Model_File = "Trained_Model/Inbuilt/trained_data"
    obj = Dataset(CSVFileName)
    X, Y = obj.read_dataset()
    xTrain, xTest, yTrain, yTest = obj.split(X, Y)
    d_tree = 0

    if uic.args.train:
        print(uic.args.train)
        model = obj.train(xTrain, yTrain)
        obj.wr_pickle(model, Trained_Model_File)
        print("Model Trained")
    elif uic.args.test:
        trained = obj.rd_pickle(Trained_Model_File)
        obj.test(trained, xTest)
        obj.score(trained, yTest)
    elif uic.args.predict:
        w, s = [], []
        w.append(uic.args.weight)
        if uic.args.surface == 'Rough':
            s.append(0)
        elif uic.args.surface== 'Smooth':
            s.append(1)
        to_predict = pd.DataFrame({
            "weight": w,
            "surface": s
        })
        # print(to_predict)
        trained = obj.rd_pickle(Trained_Model_File)
        print(obj.predict_label(trained, to_predict))
