import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def p2():
    data = pd.read_csv('wdbc.data', header=None)

    # Procesarea datelor
    X = data.iloc[:, [2, 3]].values  # raza si textura
    y = LabelEncoder().fit_transform(data.iloc[:, 1].values)  # transformam 'M' si 'B' in 1 si 0

    # Normalizarea datelor
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Impartirea datelor in seturi de antrenament si testare
    X_train, X_test, y_train, y1_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Antrenarea modelului
    model1 = LogisticRegression()
    model1.fit(X_train, y_train)


    # Testarea modelului
    print(f"Accuracy for problem 2: {model1.score(X_test, y1_test)}")

    # Predictia pt o noua leziune
    new_lesion = np.array([[18, 10]])
    prediction = model1.predict(new_lesion)
    print(f"The lesion is {'malignant' if prediction[0] == 1 else 'benign'}")


