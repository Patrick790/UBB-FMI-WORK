import random


def p1a():
    def read_corpus(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            corpus = file.read()
        return corpus

    def preprocess_text(text):
        # Indepartarea caracterelor speciale si impartirea textului in cuvinte
        text = text.replace('\n', ' ').replace('\r', '')
        words = text.split()
        return words

    def build_markov_chain(words):
        chain = {}
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            if current_word not in chain:
                chain[current_word] = [next_word]
            else:
                chain[current_word].append(next_word)
        return chain

    def generate_text(chain, length=50):
        current_word = random.choice(list(chain.keys()))
        generated_text = [current_word]
        for _ in range(length - 1):
            if current_word in chain:
                next_word = random.choice(chain[current_word])
                generated_text.append(next_word)
                current_word = next_word
                # Verificam daca cuvantul curent este sfarsit de vers
                if '\n' in current_word:
                    generated_text.append('\n')
        return ' '.join(generated_text)

    # Citim corpusul din fisier
    file_path = 'corpus'
    corpus = read_corpus(file_path)

    # Preprocesarea textului
    words = preprocess_text(corpus)
    markov_chain = build_markov_chain(words)

    # Generarea unui text
    generated_text = generate_text(markov_chain)
    print(generated_text)
