import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv("Dataset/Ball_Dataset.csv")
dataset["Surface"] = pd.factorize(dataset.Surface)[0]
dataset["Label"] = pd.factorize(dataset.Label)[0]
X = dataset.drop(["Label"], axis=1)
Y = dataset["Label"]

# Converted textual data into numbers manually
# 0 = Rough, Tennis
# 1 = Smooth, Cricket
# X = [[35, 0],
#      [47, 0],
#      [90, 1],
#      [48, 0],
#      [90, 1],
#      [35, 0],
#      [92, 1],
#      [35, 0],
#      [35, 0],
#      [35, 0],
#      [96, 1],
#      [43, 0],
#      [110, 1],
#      [35, 0],
#      [95, 1]]
# y = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]

# Splitting the data for training and testing
xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating object of decision tree
dtc = DecisionTreeClassifier()

# Fitting the training data
training = dtc.fit(xTrain, yTrain)

# predicting
yPredict = dtc.predict(xTest)

# Displaying the result
print("Input ta given to model :\n", xTest)
print("Predicted label by the model :\n", yPredict, end="\n")
