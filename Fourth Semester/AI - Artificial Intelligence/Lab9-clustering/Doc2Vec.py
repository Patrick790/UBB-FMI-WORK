import csv
import os

import numpy as np
import nltk

nltk.download('punkt')
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import word_tokenize


def doc2vec():
    # pas 1 - incarcare date
    crt_dir = os.getcwd()
    file_name = os.path.join(crt_dir, 'reviews_mixed.csv')

    data = []
    with open(file_name, encoding='ISO-8859-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                data_names = row
            else:
                data.append(row)
            line_count += 1

    inputs = [data[i][0] for i in range(len(data))][:100]
    outputs = [data[i][1] for i in range(len(data))][:100]
    label_names = list(set(outputs))

    print(inputs[:2])
    print(label_names[:2])

    # pas 2 - impartire date

    np.random.seed(5)
    no_samples = len(inputs)
    indexes = [i for i in range(no_samples)]
    train_sample = np.random.choice(indexes, int(0.8 * no_samples), replace=False)
    test_sample = [i for i in indexes if i not in train_sample]

    train_inputs = [inputs[i] for i in train_sample]
    train_outputs = [outputs[i] for i in train_sample]
    test_inputs = [inputs[i] for i in test_sample]
    test_outputs = [outputs[i] for i in test_sample]

    print(train_inputs[:3])

    # pas 3 - extragere caracteristici

    # preprocesare text
    train_corpus = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(train_inputs)]
    test_corpus = [word_tokenize(_d.lower()) for _d in test_inputs]

    # antrenare model Doc2Vec
    model = Doc2Vec(vector_size=50, min_count=2, epochs=40)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)

    # extragere caracteristici
    train_features = [model.infer_vector(doc.words) for doc in train_corpus]
    test_features = [model.infer_vector(doc) for doc in test_corpus]
    print(len(train_features[0]))

    # pas 4 - antrenare model de invatare nesupervizata (clustering)

    unsupervised_classifier = KMeans(n_clusters=2, random_state=0)
    unsupervised_classifier.fit(train_features)

    # pas 5 - testare model
    computed_test_indexes = unsupervised_classifier.predict(test_features)
    computed_test_outputs = [label_names[value] for value in computed_test_indexes]
    for i in range(0, len(test_inputs)):
        print(test_inputs[i], " -> ", computed_test_outputs[i])

    # pas 6 - calcul metrici de performanta

    print("accuracy: ", accuracy_score(test_outputs, computed_test_outputs))
