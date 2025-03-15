import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


def p1():
    class LinearRegression:
        def __init__(self, learning_rate=0.01, num_iterations=1000, batch_size=20):
            self.learning_rate = learning_rate
            self.num_iterations = num_iterations
            self.batch_size = batch_size
            self.weights = None
            self.bias = None

        def fit(self, X, y):
            num_samples, num_features = X.shape
            self.weights = np.zeros(num_features)
            self.bias = 0

            # Gradient descent
            for _ in range(self.num_iterations):
                # Shuffle the data
                indices = np.random.permutation(num_samples)
                X = X[indices]
                y = y[indices]

                # Split the data into batches
                for i in range(0, num_samples, self.batch_size):
                    X_batch = X[i:i+self.batch_size]
                    y_batch = y[i:i+self.batch_size]

                    # Compute the prediction
                    y_predicted = np.dot(X_batch, self.weights) + self.bias

                    # Ensure y_predicted and y_batch have the same shape
                    y_predicted = y_predicted.reshape(y_batch.shape)

                    # Compute the partial derivatives of the cost function with respect to the weights and bias
                    dw = (1 / self.batch_size) * np.dot(X_batch.T, (y_predicted - y_batch))
                    db = (1 / self.batch_size) * np.sum(y_predicted - y_batch)

                    # Update the weights and bias using gradient descent
                    self.weights -= self.learning_rate * dw.flatten()
                    self.bias -= self.learning_rate * db

        def predict(self, X):
            if X.shape[1] == len(self.weights):
                return np.dot(X, self.weights) + self.bias
            else:
                raise ValueError("Number of features in X does not match the number of weights")

    # Incarcarea datelor din fisierul CSV
    data = pd.read_csv('2017.csv')

    # Extragem GDP, Freedom si Happiness din setul de date
    X_gdp = data['Economy..GDP.per.Capita.'].values.reshape(-1, 1)
    X_freedom = data['Freedom'].values.reshape(-1, 1)
    y = data['Happiness.Score'].values.reshape(-1, 1)

    # Antrenarea modelului folosind doar gdp
    model_gdp = LinearRegression()
    model_gdp.fit(X_gdp, y)

    # Antrenarea modelului folosind GDP si Freedom
    X_gdp_freedom = np.column_stack((X_gdp, X_freedom))  # corect  # Adaugam datele de Freedom la matricea de
    # caracteristici
    model_gdp_freedom = LinearRegression()
    model_gdp_freedom.fit(X_gdp_freedom, y)

    # Testarea modelului
    num_test_samples = 20
    X_test_gdp = 10 * np.random.rand(num_test_samples, 1)
    X_test_freedom = 5 * np.random.rand(num_test_samples, 1)
    y_test = 2 * X_test_gdp + 3 * X_test_freedom + np.random.randn(num_test_samples, 1)

    # Plotare date de antrenare și linia de regresie
    def plot_regression_line(X, y, model, title):
        # If the model was trained with two features, we need to provide two features for prediction
        if len(model.weights) == 2:
            # Assuming the second feature (Freedom) is zero for the purpose of plotting
            X = np.column_stack((X, np.zeros_like(X)))
        plt.scatter(X[:, 0], y, color='blue', label='Data')
        plt.plot(X[:, 0], model.predict(X), color='red', linewidth=3, label='Regression Line')
        plt.title(title)
        plt.xlabel('GDP')
        plt.ylabel('Happiness')
        plt.legend()
        plt.show()

    # Plotare predictiile modelului impreuna cu datele reale
    def plot_predictions(X, y, predictions, title):
        plt.scatter(X, y, color='blue', label='Actual data')
        plt.scatter(X, predictions, color='red', label='Predictions')
        plt.title(title)
        plt.xlabel('GDP')
        plt.ylabel('Happiness')
        plt.legend()
        plt.show()

    # Plotare pentru modelul cu doar GDP
    plot_regression_line(X_gdp, y, model_gdp, 'Regression Line using GDP')

    # Plotare pentru modelul cu GDP și Freedom
    plot_regression_line(X_gdp_freedom[:, 0], y, model_gdp_freedom, 'Regression Line using GDP and Freedom')

    # Presupunem ca avem date pentru testare (X_test_gdp, X_test_freedom)
    # Folosim modelul cu doar GDP pentru a face predictii
    predicted_happiness_gdp = model_gdp.predict(X_test_gdp)

    # Plotare predictiile modelului impreuna cu datele reale pentru modelul cu doar GDP
    plot_predictions(X_test_gdp, y_test, predicted_happiness_gdp, 'Predictions using GDP')

    # Folosim modelul cu GDP și Freedom pentru a face predictii
    X_test_gdp_freedom = np.column_stack((X_test_gdp, X_test_freedom))
    predicted_happiness_gdp_freedom = model_gdp_freedom.predict(X_test_gdp_freedom)

    # Plotare predictiile modelului impreuna cu datele reale pentru modelul cu GDP și Freedom
    plot_predictions(X_test_gdp_freedom[:, 0], y_test, predicted_happiness_gdp_freedom,
                     'Predictions using GDP and Freedom')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_gdp_freedom[:, 0], X_gdp_freedom[:, 1], y, color='blue')
    ax.set_xlabel('GDP')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.show()