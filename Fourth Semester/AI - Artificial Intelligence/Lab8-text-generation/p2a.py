import markovify
from datasets import load_dataset
from textblob import TextBlob


def p2a():
    dataset = load_dataset("biglam/gutenberg-poetry-corpus")

    # Preprocesarea textului
    text = ' '.join(dataset['train']['line'])

    # Construim modelul Markov
    text_model = markovify.Text(text)

    for i in range(4):  # Generam 4 linii pentru a forma o strofa
        sentence = text_model.make_short_sentence(70)
        print(sentence)

        # Calculam sentimentul pentru fiecare linie
        blob = TextBlob(sentence)
        print(blob.sentiment)
