from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

data = pd.read_csv("Dataset/Play_Predictor.csv")
data = data.drop(["sr"], axis=1)
data["Wether"] = pd.factorize(data.Wether)[0]
data["Temperature"] = pd.factorize(data.Temperature)[0]
data["Play"] = pd.factorize(data.Play)[0]

X = data.drop(["Play"], axis=1)
Y = data["Play"]

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.2, random_state=0)

knn = KNeighborsClassifier()
train = knn.fit(xtrain, ytrain)

ypredicted = knn.predict(xtest)

acc = accuracy_score(ytest, ypredicted)

# print("0 - Sunny, Hot, No\n1 - Overcast, Mild, yes\n2 - Rainy, cool")
# print(data)
# print("---------")
# print(xtest)
# print("---------")
# print(ypredicted)
print("Accuracy Score : ", acc)
