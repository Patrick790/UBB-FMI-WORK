import os

import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import numpy as np
import re
import unidecode


# problema 1a
df_employees = pd.read_csv('employees.csv', delimiter=',', header="infer")
df_employees.head()

df_employees.isnull()

# var = df_employees[df_employees.isnull().any(axis=1)]
# print(var)

print("Numarul de angajati:", df_employees.shape[0])

# Selectăm primul angajat (rândul cu indexul 0)
employee = df_employees.iloc[0]

# Numărăm proprietățile pentru acest angajat
num_properties = len(employee)

# Afișăm numărul și tipul informatiilor (proprietatilor) pentru acest angajat
print("Numarul de proprietati pentru acest angajat:", num_properties)
print("Proprietatile pentru angajat:")
print(employee)

# Elimin randurile care conțin valori nule
complete_data = df_employees.dropna()

num_complete_employees = len(complete_data)

print("Numarul de angajați pentru care se detin date complete:", num_complete_employees)

medie_salarii = df_employees['Salary'].mean()
print("Media salarii:", medie_salarii)
max_salarii = df_employees['Salary'].max()
print("Salariul maxim:", max_salarii)
min_salarii = df_employees['Salary'].min()
print("Salariul minim:", min_salarii)

medie_bonusuri = df_employees['Bonus %'].mean()
print("Media bonusuri:", medie_bonusuri)
max_bonusuri = df_employees['Bonus %'].max()
print("Bonus maxim:", max_bonusuri)
min_bonusuri = df_employees['Bonus %'].min()
print("Bonus minim:", min_bonusuri)

# # Calculăm statistici descriptive pentru fiecare proprietate
# stats = df_employees.describe()
#
# # Afișăm statisticiile
# print("Valorile minime, maxime și medii pentru fiecare proprietate:")
# print(stats)

# Numarul de valori unice pentru fiecare proprietate nenumerica
num_unique_values = df_employees.select_dtypes(exclude='number').nunique()

# Numarul de valori unice pentru fiecare proprietate nenumerica
print("Numarul de valori unice pentru fiecare proprietate nenumerica:")
print(num_unique_values)

if df_employees.isnull().any().any():
    print("Există valori lipsă în DataFrame.")
    # Identificăm coloanele numerice
    numeric_columns = df_employees.select_dtypes(include='number').columns

    # Înlocuim valorile lipsă din coloanele numerice cu media lor
    df_employees[numeric_columns] = df_employees[numeric_columns].fillna(df_employees[numeric_columns].mean())


else:
    print("Nu există valori lipsă în DataFrame.")

# Problema 1b

# Categorii de salarii
bins = [0, 50000, 100000, 150000, 200000]
labels = ['0-50k', '50k-100k', '100k-150k', '150k-200k']
df_employees['Salary Category'] = pd.cut(df_employees['Salary'], bins=bins, labels=labels)

# Distributia salariilor
plt.figure(figsize=(10, 6))
sns.countplot(x='Salary Category', data=df_employees)
plt.title('Distribution of Salaries')
plt.show()

# Distributia salariilor pe echipe
plt.figure(figsize=(10, 6))
sns.countplot(x='Salary Category', hue='Team', data=df_employees)
plt.title('Distribution of Salaries per Team')
plt.show()

# Identificarea outlierilor
Q1 = df_employees['Salary'].quantile(0.25)
Q3 = df_employees['Salary'].quantile(0.75)
IQR = Q3 - Q1

filtrare = (df_employees['Salary'] >= Q1 - 1.5 * IQR) & (df_employees['Salary'] <= Q3 + 1.5 * IQR)
outliers = df_employees.loc[~filtrare]

plt.figure(figsize=(10, 6))
sns.boxplot(x='Salary', data=df_employees)
sns.scatterplot(x=outliers.index, y=outliers['Salary'], color='red')
plt.title('Outliers in Salaries')
plt.show()

# Problema 2

print("---------Problema 2---------")

# a)
img_path = 'images/Karpaty.jpg'
img = cv2.imread(img_path)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# b) Redimensionarea imaginilor
folder_path = 'images'
images = []
for filename in os.listdir(folder_path):
    img = cv2.imread(os.path.join(folder_path, filename))
    if img is not None:
        img = cv2.resize(img, (128, 128))
        images.append(img)

# Vizualizare imagini
fig = plt.figure(figsize=(10, 10))
columns = 5
rows = int(np.ceil(len(images) / columns))
for i, image in enumerate(images):
    fig.add_subplot(rows, columns, i + 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# c) Conversia imaginilor la alb-negru

gray_images = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in images]
fig = plt.figure(figsize=(10, 10))
for i, image in enumerate(gray_images):
    fig.add_subplot(rows, columns, i + 1)
    plt.imshow(image, cmap='gray')
plt.show()

# d) sa se blureze o imagine si sa se afiseze in format "before-after"
blur = cv2.GaussianBlur(images[0], (5, 5), 0)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(images[0], cv2.COLOR_BGR2RGB)), plt.title('Before')
plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)), plt.title('After')
plt.show()

# e) Se identifica muchiile si before and after
edges = cv2.Canny(images[0], 100, 200)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(images[0], cv2.COLOR_BGR2RGB)), plt.title('Before')
plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('After')
plt.show()


# Problema 3

# Citire text
with open('texts.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# a) Nr propozitii
propozitii = re.split(r'(?<=[.!?]) +', text)
print("Numarul de propozitii:", len(propozitii))

# b) Nr cuvinte
cuvinte = text.split()
print("Numarul de cuvinte:", len(cuvinte))

# c) Nr cuvinte diferite in text
cuvinte_diferite = set(cuvinte)
print("Numarul de cuvinte diferite:", len(cuvinte_diferite))

# d) Cel mai lung si cel mai scurt cuvant
cel_mai_lung_cuvant = max(cuvinte, key=len)
cel_mai_scurt_cuvant = min(cuvinte, key=len)
print("Cel mai lung cuvant:", cel_mai_lung_cuvant)
print("Cel mai scurt cuvant:", cel_mai_scurt_cuvant)

# e) Textul fara diacritice
text_fara_diacritice = unidecode.unidecode(text)
print("Textul fara diacritice:", text_fara_diacritice)

# f) Sinonimele celui mai lung cuvant

synonyms = []
for syn in wordnet.synsets(cel_mai_lung_cuvant):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(f"Synonyms of {cel_mai_lung_cuvant}: {synonyms}")


