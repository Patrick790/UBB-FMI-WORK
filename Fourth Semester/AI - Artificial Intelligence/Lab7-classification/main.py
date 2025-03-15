import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt


# Funcție pentru incarcarea imaginilor si etichetarea lor
def load_images_and_labels():
    sepia_images = []
    non_sepia_images = []

    # Incarca imagini cu filtru sepia
    for filename in os.listdir('sepia'):  # specifica calea catre imaginile cu sepia
        img_path = os.path.join('sepia', filename)
        if os.path.isfile(img_path):
            sepia_images.append(img_path)

    for filename in os.listdir('images'):
        img_path = os.path.join('images', filename)
        if os.path.isfile(img_path):
            non_sepia_images.append(img_path)

    # Eticheteaza imaginile: 1 pentru sepia, 0 pentru non-sepia
    sepia_labels = np.ones(len(sepia_images))
    non_sepia_labels = np.zeros(len(non_sepia_images))

    # Combina imaginile si etichetele
    images = sepia_images + non_sepia_images
    labels = list(sepia_labels) + list(non_sepia_labels)

    # Creaza un DataFrame Pandas
    data = {"Image_Path": images, "Labels": labels}
    df = pd.DataFrame(data)

    # Salveaza DataFrame-ul într-un fișier CSV
    df.to_csv("image_labels.csv", index=False)

    return df


# Functie pentru antrenarea si testarea clasificatorului ANN
def train_and_test_classifier(classifier, images, labels):
    # Imparte datele in seturi de antrenare si testare
    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2,
                                                                            random_state=42)

    # Redimensionarea si aplatizarea imaginilor
    train_images_flat = np.array([np.array(Image.open(img).resize((64, 64))).flatten() for img in train_images])
    test_images_flat = np.array([np.array(Image.open(img).resize((64, 64))).flatten() for img in test_images])

    # Antreneaza clasificatorul ANN
    classifier.fit(train_images_flat, train_labels)

    # Predictia etichetelor pt setul de testare
    predicted_labels = classifier.predict(test_images_flat)

    # Evaluarea performantei clasificatorului
    accuracy = accuracy_score(test_labels, predicted_labels)
    precision = precision_score(test_labels, predicted_labels)
    recall = recall_score(test_labels, predicted_labels)
    confusion = confusion_matrix(test_labels, predicted_labels)

    return accuracy, precision, recall, confusion


def evaluate_parameters(images, labels, hidden_layer_sizes):
    accuracies = []
    precisions = []
    recalls = []
    for size in hidden_layer_sizes:
        # Initializeaza si antreneaza clasificatorul ANN cu parametrii modificati
        classifier = MLPClassifier(hidden_layer_sizes=size, activation='relu', max_iter=100, solver='adam',
                                   random_state=42)
        accuracy, precision, recall, _ = train_and_test_classifier(classifier, images, labels)
        accuracies.append(accuracy)
        precisions.append(precision)
        recalls.append(recall)
    return accuracies, precisions, recalls


def main():
    # Incarca imagini si etichete si creeaza baza de date
    df = load_images_and_labels()

    # Extrage calea catre imagini și etichetele corespunzătoare
    images = df["Image_Path"]
    labels = df["Labels"]

    # Definiti o serie de valori pentru parametrul hidden_layer_sizes
    hidden_layer_sizes = [(50,), (100,), (150,), (200,)]

    # Initializeaza si antreneaza clasificatorul ANN
    classifier = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', max_iter=100, solver='adam',
                               random_state=42)
    accuracy, precision, recall, confusion = train_and_test_classifier(classifier, images, labels)

    # Afisează rezultatele
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("Confusion Matrix:")
    print(confusion)

    # Afiseaza matricea de confuzie
    plt.imshow(confusion, cmap='Blues')
    plt.colorbar()
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.show()
    # Evaluarea influentei parametrului hidden_layer_sizes
    accuracies, precisions, recalls = evaluate_parameters(images, labels, hidden_layer_sizes)

    # Afisarea rezultatelor
    for i, size in enumerate(hidden_layer_sizes):
        print(
            f"Hidden Layer Sizes: {size}, Accuracy: {accuracies[i]}, Precision: {precisions[i]}, Recall: {recalls[i]}")


if __name__ == "__main__":
    main()
