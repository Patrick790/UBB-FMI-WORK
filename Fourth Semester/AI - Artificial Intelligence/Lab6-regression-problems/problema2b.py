import numpy as np
import pandas as pd


def sigmoid(z):  # transforma scorurile brute in probabilitati
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


def normalize(trainData, testData):
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

    return np.array(normalisedTrainData), np.array(normalisedTestData)


def p2():
    data = pd.read_csv('wdbc.data', header=None)

    # Procesarea datelor
    X = data.iloc[:, [2, 3]].values  # raza si textura
    y = data.iloc[:, 1].replace(['M', 'B'], [1, 0]).values  # transformam 'M' si 'B' in 1 si 0

    # Impartirea datelor in seturi de antrenament si testare
    train_size = int(0.8 * len(y))  # 80% din date pt antrenare
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Normalizarea datelor
    X_train, X_test = normalize(X_train, X_test)

    # Antrenarea modelului
    weights = np.zeros(X_train.shape[1])
    weights = gradient_descent(X_train, y_train, weights, learning_rate=0.1, iterations=2000)

    # Testarea modelului
    y_pred = sigmoid(np.dot(X_test, weights))
    y_pred = [1 if p >= 0.5 else 0 for p in y_pred]
    accuracy = np.mean(y_pred == y_test)
    print(f"Accuracy for problem 2: {accuracy}")

    # Predictia pt o noua leziune
    new_lesion = np.array([18, 10])
    new_lesion = (new_lesion - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)
    prediction = sigmoid(np.dot(new_lesion, weights))
    prediction = 1 if prediction >= 0.5 else 0
    print(f"The lesion is {'malignant' if prediction == 1 else 'benign'}")
