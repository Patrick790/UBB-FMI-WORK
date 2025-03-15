import numpy as np
import pandas as pd
import warnings
from sklearn.metrics import mean_squared_error

warnings.filterwarnings('ignore', category=FutureWarning)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost_function(X, y, weights):
    z = np.dot(X, weights)
    predict_1 = y * np.log(sigmoid(z))
    predict_0 = (1 - y) * np.log(1 - sigmoid(z))
    return -sum(predict_1 + predict_0) / len(X)


def gradient_descent(X, y, weights, learning_rate, iterations):
    for i in range(iterations):
        z = np.dot(X, weights)
        prediction = sigmoid(z)
        gradient = np.dot(X.T, (prediction - y)) / y.size
        weights -= learning_rate * gradient
    return weights


def normalize(trainData, testData, mean=None, std=None):
    if mean is None or std is None:
        mean = np.mean(trainData, axis=0)
        std = np.std(trainData, axis=0)

    if not isinstance(trainData[0], list):
        #encode each sample into a list
        trainData = [[d] for d in trainData]
        testData = [[d] for d in testData]

        normalisedTrainData = (trainData - mean) / std
        normalisedTestData = (testData - mean) / std

        #decode from list to raw values
        normalisedTrainData = [el[0] for el in normalisedTrainData]
        normalisedTestData = [el[0] for el in normalisedTestData]
    else:
        normalisedTrainData = (trainData - mean) / std
        normalisedTestData = (testData - mean) / std

    return np.array(normalisedTrainData), np.array(normalisedTestData), mean, std


def p3b():
    data = pd.read_csv('iris.data', header=None)

    # Procesarea datelor
    X = data.loc[:, 0:3].values  # caracteristicile florii
    y = data.loc[:, 4].replace(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [0, 1, 2]).values

    # Impartirea datelor in seturi de antrenare si testare
    train_size = int(0.8 * len(y))  # 80% din date pentru antrenare
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Normalizarea datelor
    X_train, X_test, mean, std = normalize(X_train, X_test)

    # Antrenarea modelului
    weights = np.zeros((X_train.shape[1], 3))  # 3 greutati pentru cele 3 clase
    for i in range(3):  # Antrenam un model pentru fiecare clasa
        y_train_class = (y_train == i).astype(int)  # Etichete binare pentru clasa i
        weights[:, i] = gradient_descent(X_train, y_train_class, np.zeros(X_train.shape[1]), learning_rate=0.1,
                                         iterations=2000)

    # Testarea modelului
    y_pred = sigmoid(np.dot(X_test, weights))
    predicted_classes = np.argmax(y_pred, axis=1)
    accuracy = np.mean(predicted_classes == y_test)
    print(f"Accuracy for problem 3: {accuracy}")
    print(mean_squared_error(y_test, predicted_classes))

    # Predictia pt o noua floare
    new_flower = np.array([5.35, 3.85, 1.25, 0.4])
    new_flower = normalize(X_train, [new_flower], mean, std)[1][0]
    prediction = np.argmax(sigmoid(np.dot(new_flower, weights)))
    print(f"The flower is of species {['setosa', 'versicolor', 'virginica'][prediction]}")
