import itertools
from random import choices, sample
from math import comb, perm
from random import randrange
from matplotlib.pyplot import bar, hist, grid, show, legend
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt


def estim(nr_sim):
    urna = ['rosie'] * 5 + ['albastra'] * 3 + ['verde'] * 2
    num_events_A_B = 0
    num_events_A = 0

    for _ in range(nr_sim):
        extrageri = sample(urna, 3)

        if len(set(extrageri)) == 1:
            num_events_A_B += 1

        if 'rosie' in extrageri:
            num_events_A += 1

    return num_events_A_B / num_events_A


def prob_teoretica():
    bile_rosii = 5
    bile_albastre = 3
    bile_verzi = 2

    total_combinari = comb(10, 3)
    comb_toate_rosii = comb(bile_rosii, 3) / total_combinari
    p_a = 1 - comb(bile_rosii, 3) / total_combinari

    return comb_toate_rosii / p_a


def aruncare_zar():
    # Simulăm aruncarea zarului de 500 de ori și stocăm rezultatele într-o listă
    data = [randrange(1, 7) for _ in range(500)]

    # Definim marginile fiecărei bare ale histogramei
    bin_edges = [k + 0.5 for k in range(1, 7)]

    # Desenăm histograma cu frecvențe relative
    hist(data, bins=bin_edges, density=True, rwidth=0.9, color='green', edgecolor='black', alpha=0.5,
         label='frecvente relative')

    # Definim distribuția teoretică a probabilităților pentru un zar obișnuit
    distribution = {i: 1 / 6 for i in range(1, 7)}
    # distribution = dict([(i, 1 / 6) for i in range(1, 7)])
    # Desenăm barele pentru probabilitățile teoretice
    bar(distribution.keys(), distribution.values(), width=0.85, color='red', edgecolor='black', alpha=0.6,
        label='probabilitati')

    # Adăugăm legenda și grila
    legend(loc='lower left')
    grid()

    # Afișăm graficul
    show()


def problema_3():
    n = 5
    p = 0.6
    valori_X = binom.rvs(n, p, size=1000)

    # Calculăm histograma
    plt.hist(valori_X, bins=range(0, 6), density=True, rwidth=0.8, alpha=0.5, color='green', edgecolor='black',
             label='frecvente relative')

    # Calculăm valorile teoretice folosind distribuția binomială
    valori_teorice = [binom.pmf(x, n, p) for x in range(0, 6)]
    plt.bar(range(0, 6), valori_teorice, width=0.8, color='red', edgecolor='black', alpha=0.6, label='probabilitati')

    # Afișăm legenda și grila
    plt.legend(loc='upper right')
    plt.grid()

    # Afișăm histograma
    plt.show()

    probabilitate_estimata = binom.cdf(5, n, p) - binom.cdf(2, n, p)
    print(f"Estimarea probabilității P(2 < X ≤ 5): {probabilitate_estimata:.4f}")

    # Calculăm valoarea teoretică
    valoare_teorica = sum([binom.pmf(x, n, p) for x in range(2, 6)])
    print(f"Valoarea teoretică a probabilității P(2 < X ≤ 5): {valoare_teorica:.4f}")


def probl_4():
    data = [sum(choices(range(1, 7), k=3)) for k in range(1000)]
    bin_edges = [k + 0.5 for k in range(2, 19)]
    hist(data, bin_edges, density=True, rwidth=0.9, color='green', edgecolor='black', alpha=0.5,
         label='frecvente relative')
    distribution = dict([i, 0] for i in range(3, 19))
    for z in itertools.product(range(1, 7), repeat=3):
        distribution[sum(z)] += 1 / 216

    bar(distribution.keys(), distribution.values(), width=0.85, color='red', edgecolor='black', alpha=0.6,
        label='probabilitati')
    legend(loc='lower left')
    grid()
    show()



def main():
    nr_sim = int(input("Numar de simulari: "))
    estimated_probability = estim(nr_sim)
    print(f"Estimarea probabilității P(B|A) prin simulări: {estimated_probability}")
    theoretical_probability = prob_teoretica()
    print(f"Valoarea teoretică a probabilității P(B|A): {theoretical_probability}")
    aruncare_zar()
    problema_3()
    probl_4()


main()
