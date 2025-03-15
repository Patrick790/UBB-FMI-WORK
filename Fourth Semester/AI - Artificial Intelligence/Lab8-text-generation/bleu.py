from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import word_tokenize


def bleu():
    poetry = ("Now hath the poet's initial vision./There was a fairy./Alone unchanged, the waters of Oceanus to bring "
              "thee nearer to him./Throw empires, and Mankind's Delight!")

    reference_poetry = ("Now the initial vision of the poet has./There was a fairy./Alone unchanged, the waters of "
                        "Oceanus to bring thee nearer to him./Cast empires, and Mankind's Delight!")

    # Tokenizare
    poetry_tokens = word_tokenize(poetry.lower())
    reference_tokens = word_tokenize(reference_poetry.lower())

    # Calcul scor BLEU
    bleu_score = corpus_bleu([[reference_tokens]], [poetry_tokens])

    print("Scorul BLEU pentru poezia dată este:", bleu_score)
