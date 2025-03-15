import random


def p1b(n):
    def read_corpus(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            corpus = file.read()
        return corpus

    def preprocess_text(text):
        # Indepartarea caracterelor speciale si impartirea textului in cuvinte
        text = text.replace('\n', ' ').replace('\r', '')
        words = text.split()
        return words

    def build_markov_chain(words, n):
        chain = {}
        for i in range(len(words) - n):
            current_state = tuple(words[i:i + n])
            next_word = words[i + n]
            if current_state not in chain:
                chain[current_state] = [next_word]
            else:
                chain[current_state].append(next_word)
        return chain

    def generate_text(chain, length=50):
        current_state = random.choice(list(chain.keys()))
        generated_text = list(current_state)
        for _ in range(length - len(current_state)):
            if current_state in chain:
                next_word = random.choice(chain[current_state])
                generated_text.append(next_word)
                current_state = tuple(generated_text[-n:])
                # Verificam daca cuvantul curent este sfarsit de vers
                if '\n' in next_word:
                    generated_text.append('\n')
        return ' '.join(generated_text)

    # Citim corpusul din fisier
    file_path = 'corpus'
    corpus = read_corpus(file_path)

    # Preprocesarea textului
    words = preprocess_text(corpus)
    markov_chain = build_markov_chain(words, n)

    # Generarea unui text
    generated_text = generate_text(markov_chain, length=100)
    print(generated_text)
