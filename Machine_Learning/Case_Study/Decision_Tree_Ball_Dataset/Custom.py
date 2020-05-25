import pickle
import pandas as pd

from sklearn.metrics import accuracy_score

from commands import userInput as uic

training_data = [
    [35, "Rough", "Tennis"],
    [47, "Rough", "Tennis"],
    [90, "Smooth", "Cricket"],
    [48, "Rough", "Tennis"],
    [90, "Smooth", "Cricket"],
    [35, "Rough", "Tennis"],
    [92, "Smooth", "Cricket"],
    [35, "Rough", "Tennis"],
    [35, "Rough", "Tennis"],
    [35, "Rough", "Tennis"],
    [96, "Smooth", "Cricket"],
    [43, "Rough", "Tennis"],
]

# Column labels.
header = ["weight", "surface", "label"]


def unique_vals(rows, col):
    return set([row[col] for row in rows])


def class_counts(rows):
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)


class Question:

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))


def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def gini(rows):
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2
    return impurity


def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


def find_best_split(rows):
    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1

    for col in range(n_features):

        values = set([row[col] for row in rows])

        for val in values:

            question = Question(col, val)

            true_rows, false_rows = partition(rows, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)


class Decision_Node:
    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def build_tree(rows):
    gain, question = find_best_split(rows)
    if gain == 0:
        return Leaf(rows)
    true_rows, false_rows = partition(rows, question)

    true_branch = build_tree(true_rows)

    false_branch = build_tree(false_rows)

    return Decision_Node(question, true_branch, false_branch)


def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions

    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs


def wr_pickle(train, model):
    # creating pickle file
    outfile = open(model, 'wb')
    # saving trained model in pickle file
    pickle.dump(train, outfile)
    outfile.close()


def rd_pickle(model):
    # opening pickle file
    infile = open(model, 'rb')
    # loading the saved model into variable newTraining
    newTraining = pickle.load(infile)
    return newTraining


if __name__ == '__main__':

    Trained_Model_File = "Trained_Model/Custom/trained_data"
    # my_tree = None

    if uic.args.train:
        my_tree = build_tree(training_data)
        wr_pickle(my_tree, Trained_Model_File)
        print("Model Trained")
    elif uic.args.test:
        my_tree = rd_pickle(Trained_Model_File)
        testing_data = [
            [110, "Smooth", "Cricket"],
            [35, "Rough", "Tennis"],
            [95, "Smooth", "Cricket"],
        ]
        actual, predicted = [], []
        for row in testing_data:
            actual.append(row[-1])
            temp = print_leaf(classify(row, my_tree))
            key = list(temp)
            predicted.append(key[0])
            # print("Actual: %s. Predicted: %s" %(row[-1], print_leaf(classify(row, my_tree))))
        actual = pd.factorize(actual)[0]
        predicted = pd.factorize(predicted)[0]
        print("Model Tested")
        print("Accuracy of the model : ", accuracy_score(actual, predicted, sample_weight=None)*100)
    elif uic.args.predict:
        my_tree = rd_pickle(Trained_Model_File)
        input_data = []
        temp = [uic.args.weight, uic.args.surface]
        # input_data.append(temp)
        lable = print_leaf(classify(temp, my_tree))
        lable = list(lable)
        print(lable[0])