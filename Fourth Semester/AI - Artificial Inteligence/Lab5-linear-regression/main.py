import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

print("Rezolvarea problemei (pt datele v1) cu tool")
print("a")
print()


def load_data(fileName, inputVariabName, outputVariabName):
    # Load data from csv file
    data = []
    data_names = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                data_names = row
            else:
                data.append(row)
            line_count += 1

    selected_variable = data_names.index(inputVariabName)
    inputs = [float(data[i][selected_variable]) for i in range(len(data))]
    selected_output = data_names.index(outputVariabName)
    outputs = [float(data[i][selected_output]) for i in range(len(data))]

    return inputs, outputs


crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'v1_world-happiness-report-2017.csv')

inputs, outputs = load_data(filePath, 'Family', 'Happiness.Score')
print('in: ', inputs[:5])
print('out: ', outputs[:5])


def plot_data_family_histogram(x, variableName):
    n, bins, patches = plt.hist(x, 10, facecolor='blue', alpha=0.5)
    plt.title('Histogram of ' + variableName)
    plt.show()


plot_data_family_histogram(inputs, 'Family')
plot_data_family_histogram(outputs, 'Happiness.Score')

plt.plot(inputs, outputs, 'ro')
plt.xlabel('Family')
plt.ylabel('Happiness')
plt.title('Family vs Happiness')
plt.show()

# Pas 2
# Split the Data Into Training and Test Subsets
# In this step we will split our dataset into training and testing subsets (in proportion 80/20%).

# Training data set is used for learning the linear model. Testing dataset is used for validating of the model. All
# data from testing dataset will be new to model, and we may check how accurate are model predictions.

np.random.seed(5)
indexes = [i for i in range(len(inputs))]
trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
validationSample = [i for i in indexes if not i in trainSample]

trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]

validationInputs = [inputs[i] for i in validationSample]
validationOutputs = [outputs[i] for i in validationSample]

plt.plot(trainInputs, trainOutputs, 'ro', label='training data')  # train data are plotted by red and circle sign
plt.plot(validationInputs, validationOutputs, 'g^',
         label='validation data')  # test data are plotted by green and a triangle sign
plt.title('train and validation data')
plt.xlabel('Family')
plt.ylabel('happiness')
plt.legend()
plt.show()

# learning step: init and train a linear regression model y = f(x) = w0 + w1 * x
# Prediction step: used the trained model to estimate the output for a new input

# using sklearn training data preparation (the sklearn linear model requires as input training data as noSamples x
# noFeatures array; in the current case, the input must be a matrix of len(trainInputs) lineas and one columns (a
# single feature is used in this problem))
xx = [[el] for el in trainInputs]

# model initialisation
regressor = linear_model.LinearRegression()
# training the model by using the training inputs and known training outputs
regressor.fit(xx, trainOutputs)
# save the model parameters
w0, w1 = regressor.intercept_, regressor.coef_[0]
print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x')

# # using developed code
# from myRegression import MyLinearUnivariateRegression

# # model initialisation
# regressor = MyLinearUnivariateRegression()
# # training the model by using the training inputs and known training outputs
# regressor.fit(trainInputs, trainOutputs)
# # save the model parameters
# w0, w1 = regressor.intercept_, regressor.coef_
# print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x')


# plot the learnt model
# prepare some synthetic data (inputs are random, while the outputs are computed by the learnt model)
noOfPoints = 1000
xref = []
val = min(trainInputs)
step = (max(trainInputs) - min(trainInputs)) / noOfPoints
for i in range(1, noOfPoints):
    xref.append(val)
    val += step
yref = [w0 + w1 * el for el in xref]

plt.plot(trainInputs, trainOutputs, 'ro', label='training data')  # train data are plotted by red and circle sign
plt.plot(xref, yref, 'b-', label='learnt model')  # model is plotted by a blue line
plt.title('train data and the learnt model')
plt.xlabel('Family')
plt.ylabel('happiness')
plt.legend()
plt.show()

# use the trained model to predict new inputs

# makes predictions for test data (manual)
# computedTestOutputs = [w0 + w1 * el for el in testInputs]

# makes predictions for test data (by tool)
computedValidationOutputs = regressor.predict([[x] for x in validationInputs])

# plot the computed outputs (see how far they are from the real outputs)
plt.plot(validationInputs, computedValidationOutputs, 'yo',
         label='computed test data')  # computed test data are plotted yellow red and circle sign
plt.plot(validationInputs, validationOutputs, 'g^',
         label='real test data')  # real test data are plotted by green triangles
plt.title('computed validation and real validation data')
plt.xlabel('Family')
plt.ylabel('happiness')
plt.legend()
plt.show()

# compute the differences between the predictions and real outputs
# "manual" computation
error = 0.0
for t1, t2 in zip(computedValidationOutputs, validationOutputs):
    error += (t1 - t2) ** 2
error = error / len(validationOutputs)
print('prediction error (manual): ', error)

# by using sklearn
from sklearn.metrics import mean_squared_error

error = mean_squared_error(validationOutputs, computedValidationOutputs)
print('prediction error (tool):  ', error)

print()
print("b")
print()


def load_data2(fileName, inputVariabNames, outputVariabName):
    data = []
    data_names = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                data_names = row
            else:
                data.append(row)
            line_count += 1

    selected_variables = [data_names.index(var) for var in inputVariabNames]
    inputs = [[float(data[i][var]) if data[i][var] != '' else 0.0 for var in selected_variables] for i in
              range(len(data))]
    selected_output = data_names.index(outputVariabName)
    outputs = [float(data[i][selected_output]) for i in range(len(data))]

    return inputs, outputs


# Load data
filePath = "v1_world-happiness-report-2017.csv"
inputs, outputs = load_data2(filePath, ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')


def plot_data_3d(inputs, outputs, variable_names):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [input[0] for input in inputs]
    y = [input[1] for input in inputs]
    ax.scatter(x, y, outputs, c='r', marker='o')
    ax.set_xlabel(variable_names[0])
    ax.set_ylabel(variable_names[1])
    ax.set_zlabel('Happiness Score')
    plt.title('3D Plot of Data')
    plt.show()


plot_data_3d(inputs, outputs, ['GDP capita', 'Freedom'])

# Train-test split
np.random.seed(5)
indexes = [i for i in range(len(inputs))]
trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
validationSample = [i for i in indexes if not i in trainSample]

trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]

validationInputs = [inputs[i] for i in validationSample]
validationOutputs = [outputs[i] for i in validationSample]

# Model initialization and training
regressor2 = linear_model.LinearRegression()
regressor2.fit(trainInputs, trainOutputs)


# Plot 3D model predictions
def plot_model_3d(inputs, outputs, model, variable_names):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [input[0] for input in inputs]
    y = [input[1] for input in inputs]
    z = model.predict(inputs)
    ax.scatter(x, y, z, c='b', marker='^')
    ax.set_xlabel(variable_names[0])
    ax.set_ylabel(variable_names[1])
    ax.set_zlabel('Predicted Happiness Score')
    plt.title('3D Plot of Model Predictions')
    plt.show()


plot_model_3d(validationInputs, validationOutputs, regressor2, ['GDP capita', 'Freedom'])

# Compute and print prediction error
computedValidationOutputs = regressor2.predict(validationInputs)
error = mean_squared_error(validationOutputs, computedValidationOutputs)
print('Prediction error (tool): ', error)

print()
print("Rezolvarea problemei (pt datele v1) cu cod propriu ")
print()


def load_data3(fileName, inputVarName, outputVarName):
    data = []
    with open(fileName, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # get header
        input_index = header.index(inputVarName)
        output_index = header.index(outputVarName)
        for row in csv_reader:
            data.append((float(row[input_index]), float(row[output_index])))
    return data


def split_data(data, split_ratio):
    train_size = int(len(data) * split_ratio)
    train_set = data[:train_size]
    test_set = data[train_size:]
    return train_set, test_set


def train_model(train_data):
    x = [row[0] for row in train_data]
    y = [row[1] for row in train_data]
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    denominator = sum((xi - x_mean) ** 2 for xi in x)

    # Check if the denominator is zero
    if denominator == 0:
        # Handle the special case where all x values are the same
        w1 = 0
    else:
        w1 = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / denominator

    w0 = y_mean - w1 * x_mean
    return w0, w1


def predict(model, x):
    w0, w1 = model
    return w0 + w1 * x


def compute_error(model, test_data):
    return sum((yi - predict(model, xi)) ** 2 for xi, yi in test_data) / len(test_data)


# Load and split the data
data = load_data3('v1_world-happiness-report-2017.csv', 'Economy..GDP.per.Capita.', 'Happiness.Score')
train_data, test_data = split_data(data, 0.8)

# Train the model
model = train_model(train_data)

# Compute the prediction error
error = compute_error(model, test_data)
print('Prediction error: ', error)

# Extract x and y values from test data
x_test = [xi for xi, _ in test_data]
y_test = [yi for _, yi in test_data]

# Use the trained model to predict y values
y_pred = [predict(model, xi) for xi in x_test]

# Plot actual y values
plt.scatter(x_test, y_test, color='blue', label='Actual')

# Plot predicted y values
plt.scatter(x_test, y_pred, color='red', label='Predicted')

# Add labels and title
plt.xlabel('Economy..GDP.per.Capita.')
plt.ylabel('Happiness.Score')
plt.title('Actual vs Predicted Happiness Score')
plt.legend()

# Display the plot
plt.show()

print()
print("Rezolvarea problemei (pt datele v2)")
print()

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'v2_world-happiness-report-2017.csv')

inputs, outputs = load_data(filePath, 'Family', 'Happiness.Score')
print('in: ', inputs[:5])
print('out: ', outputs[:5])

plot_data_family_histogram(inputs, 'Family')
plot_data_family_histogram(outputs, 'Happiness.Score')

plt.plot(inputs, outputs, 'ro')
plt.xlabel('Family')
plt.ylabel('Happiness')
plt.title('Family vs Happiness')
plt.show()

np.random.seed(5)
indexes = [i for i in range(len(inputs))]
trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
validationSample = [i for i in indexes if not i in trainSample]

trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]

validationInputs = [inputs[i] for i in validationSample]
validationOutputs = [outputs[i] for i in validationSample]

plt.plot(trainInputs, trainOutputs, 'ro', label='training data')  # train data are plotted by red and circle sign
plt.plot(validationInputs, validationOutputs, 'g^',
         label='validation data')  # test data are plotted by green and a triangle sign
plt.title('train and validation data')
plt.xlabel('Family')
plt.ylabel('happiness')
plt.legend()
plt.show()

xx = [[el] for el in trainInputs]

# model initialisation
regressor = linear_model.LinearRegression()
# training the model by using the training inputs and known training outputs
regressor.fit(xx, trainOutputs)
# save the model parameters
w0, w1 = regressor.intercept_, regressor.coef_[0]
print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x')

# plot the learnt model
# prepare some synthetic data (inputs are random, while the outputs are computed by the learnt model)
noOfPoints = 1000
xref = []
val = min(trainInputs)
step = (max(trainInputs) - min(trainInputs)) / noOfPoints
for i in range(1, noOfPoints):
    xref.append(val)
    val += step
yref = [w0 + w1 * el for el in xref]

plt.plot(trainInputs, trainOutputs, 'ro', label='training data')  # train data are plotted by red and circle sign
plt.plot(xref, yref, 'b-', label='learnt model')  # model is plotted by a blue line
plt.title('train data and the learnt model')
plt.xlabel('Family')
plt.ylabel('happiness')
plt.legend()
plt.show()

# makes predictions for test data (by tool)
computedValidationOutputs = regressor.predict([[x] for x in validationInputs])

# plot the computed outputs (see how far they are from the real outputs)
plt.plot(validationInputs, computedValidationOutputs, 'yo',
         label='computed test data')  # computed test data are plotted yellow red and circle sign
plt.plot(validationInputs, validationOutputs, 'g^',
         label='real test data')  # real test data are plotted by green triangles
plt.title('computed validation and real validation data')
plt.xlabel('Family')
plt.ylabel('happiness')
plt.legend()
plt.show()

# compute the differences between the predictions and real outputs
# "manual" computation
error = 0.0
for t1, t2 in zip(computedValidationOutputs, validationOutputs):
    error += (t1 - t2) ** 2
error = error / len(validationOutputs)
print('prediction error (manual): ', error)

# by using sklearn
from sklearn.metrics import mean_squared_error

error = mean_squared_error(validationOutputs, computedValidationOutputs)
print('prediction error (tool):  ', error)

######################### 3b

inputs, outputs = load_data2(filePath, ['Economy..GDP.per.Capita.', 'Freedom'], 'Happiness.Score')
print('in:  ', inputs[:5])
print('out: ', outputs[:5])

# plot_data_freedom_histogram(inputs, ['Economy..GDP.per.Capita.', 'Freedom'])
# plot_data_freedom_histogram(outputs, 'Happiness score')
plot_data_3d(inputs, outputs, ['GDP capita', 'Freedom'])

plt.plot(inputs, outputs, 'ro')
plt.xlabel('GDP capita, Freedom')
plt.ylabel('happiness')
plt.title('GDP capita and Freedom vs. happiness')
plt.show()

np.random.seed(5)
indexes = [i for i in range(len(inputs))]
trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
validationSample = [i for i in indexes if not i in trainSample]

trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]

validationInputs = [inputs[i] for i in validationSample]
validationOutputs = [outputs[i] for i in validationSample]

plt.plot(trainInputs, trainOutputs, 'ro', label='training data')  # train data are plotted by red and circle sign
plt.plot(validationInputs, validationOutputs, 'g^',
         label='validation data')  # test data are plotted by green and a triangle sign
plt.title('train and validation data')
plt.xlabel('GDP capita and Freedom')
plt.ylabel('happiness')
plt.legend()
plt.show()

xx = [[el] for el in trainInputs]

# model initialisation
regressor2 = linear_model.LinearRegression()
# training the model by using the training inputs and known training outputs
regressor2.fit(trainInputs, trainOutputs)
# save the model parameters
w0, w1 = regressor2.intercept_, regressor2.coef_[0]
print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x')
noOfPoints = 1000
xref = []

# Calculate the min and max for each feature
min_values = [min(feature) for feature in zip(*trainInputs)]
max_values = [max(feature) for feature in zip(*trainInputs)]

# Calculate the step size for each feature
step_sizes = [(max_val - min_val) / noOfPoints for max_val, min_val in zip(max_values, min_values)]

# Generate the sequence of values for each feature
for step in step_sizes:
    val = min_values[step_sizes.index(step)]
    for i in range(1, noOfPoints):
        xref.append(val)
        val += step

# Generate yref using the linear regression model parameters
yref = [w0 + w1 * el for el in xref]

plt.plot(trainInputs, trainOutputs, 'ro', label='training data')  # train data are plotted by red and circle sign
plt.plot(xref, yref, 'b-', label='learnt model')  # model is plotted by a blue line
plt.title('train data and the learnt model')
plt.xlabel('GDP capita and Freedom')
plt.ylabel('happiness')
plt.legend()
plt.show()

computedValidationOutputs = regressor2.predict(validationInputs)

# plot the computed outputs (see how far they are from the real outputs)
plt.plot(validationInputs, computedValidationOutputs, 'yo',
         label='computed test data')  # computed test data are plotted yellow red and circle sign
plt.plot(validationInputs, validationOutputs, 'g^',
         label='real test data')  # real test data are plotted by green triangles
plt.title('computed validation and real validation data')
plt.xlabel('GDP capita and Freedom')
plt.ylabel('happiness')
plt.legend()
plt.show()

# compute the differences between the predictions and real outputs
# "manual" computation
error = 0.0
for t1, t2 in zip(computedValidationOutputs, validationOutputs):
    error += (t1 - t2) ** 2
error = error / len(validationOutputs)
print('prediction error (manual): ', error)

error = mean_squared_error(validationOutputs, computedValidationOutputs)
print('prediction error (tool):  ', error)
