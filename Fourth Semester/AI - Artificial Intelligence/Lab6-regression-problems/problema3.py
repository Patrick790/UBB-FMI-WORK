import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def p3():
    data = pd.read_csv('iris.data', header=None)

    # Procesarea datelor
    X = data.loc[:, 0:3].values  # caracteristicile florii
    y = LabelEncoder().fit_transform(data.loc[:, 4])  # transform speciile in numere

    # Normalizarea datelor
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Impartirea datelor in seturi de antrenare si testare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Antrenarea modelului
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Testarea modelului
    print(f"Accuracy for problem 3: {model.score(X_test, y_test)}")

    # Predictia pt o noua floare
    new_flower = np.array([[5.35, 3.85, 1.25, 0.4]])
    new_flower = scaler.transform(new_flower)
    prediction = model.predict(new_flower)
    print(f"The flower is of species {['setosa', 'versicolor', 'virginica'][prediction[0]]}")