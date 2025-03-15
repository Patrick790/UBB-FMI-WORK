import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D


def p1b():
    # Load the data
    data = pd.read_csv('2017.csv')

    # Extract GDP, Freedom and Happiness from the dataset
    X = data[['Economy..GDP.per.Capita.', 'Freedom']]
    y = data['Happiness.Score']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalize the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train the model using GDP and Freedom
    model = SGDRegressor()
    batch_size = 20
    for i in range(0, X_train.shape[0], batch_size):
        X_batch = X_train[i:i + batch_size]
        y_batch = y_train[i:i + batch_size]
        model.partial_fit(X_batch, y_batch)

    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # The mean squared error
    print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_train[:, 0], X_train[:, 1], y_train, color='blue', label='Training data')
    ax.scatter(X_test[:, 0], X_test[:, 1], y_test, color='green', label='Testing data')
    ax.set_xlabel('GDP')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness')
    ax.legend()
    plt.show()


p1b()
