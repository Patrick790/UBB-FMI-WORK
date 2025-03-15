import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import Adam


def ann_tool():
    # Incarcarea datelor
    df = pd.read_csv('baza_de_date.csv')

    # Conversia imaginilor din string-uri in liste de numere
    df['Images'] = df['Images'].apply(lambda x: np.array(eval(x)))

    # Crearea seturilor de date
    X = np.stack(df['Images'].values)
    y = df['Labels'].values

    # Impartirea datelor in seturi de antrenament si de testare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalizarea datelor de intrare
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    # Crearea modelului
    model = Sequential()
    model.add(Flatten(input_shape=X_train.shape[1:]))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compilarea modelului
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

    # Antrenarea modelului
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    # Evaluarea modelului
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test accuracy: {accuracy}')
