import numpy as np
from scipy.stats import bernoulli, hypergeom, geom
import matplotlib.pyplot as plt
from math import comb


def deplasare_linie_deapta(p, num_pasi):
    pozitii = [0]
    for _ in range(num_pasi):
        directie = bernoulli.rvs(p)  # 1 pentru dreapta, 0 pentru stanga
        pas = 2 * directie - 1  # transformăm 1 în 1 și 0 în -1
        pozitii.append(pozitii[-1] + pas)
    return pozitii


def deplasare_pe_cerc(p, num_pasi, n):
    pozitii = [0]
    for _ in range(num_pasi):
        directie = bernoulli.rvs(p)
        pas = 2 * directie - 1
        pozitii.append((pozitii[-1] + pas) % n)
    return pozitii


def simulare_histograma(num_simulari, num_pasi, p, n=None):
    pozitii_finale = []
    for _ in range(num_simulari):
        if n is None:
            pozitii = deplasare_linie_deapta(p, num_pasi)

        else:
            pozitii = deplasare_pe_cerc(p, num_pasi, n)
        pozitii_finale.append(pozitii[-1])

    plt.hist(pozitii_finale, bins=range(min(pozitii_finale), max(pozitii_finale) + 2), align='left', rwidth=0.8)
    plt.xlabel('Pozitie finala')
    plt.ylabel('Frecventa')
    plt.title('Histograma pozitiilor finale')
    plt.grid(True)
    plt.show()


def simulare_loto(probabilitate_castig, num_simulari):
    rezultate = []
    for _ in range(num_simulari):
        bilete_necastigatoare = 0
        while True:
            bilete_necastigatoare += 1
            castig = hypergeom.rvs(49, 6, 6, size=1)[0]  # Extragem 6 numere din 49
            if castig >= 3:
                break
        rezultate.append(bilete_necastigatoare)
    return rezultate


def main():
    pasi = int(input("Nr pasi: "))
    pasi_linie_dreapta = deplasare_linie_deapta(0.7, pasi)
    print("a) Simulare deplasare pe linie dreapta:", pasi_linie_dreapta)

    simulare_histograma(1000, pasi, 0.7)

    simulare_histograma(100, pasi, 0.7, 10)

    # i) Generare lista pentru fiecare simulare
    rezultate_simulare = simulare_loto(probabilitate_castig=1 / comb(49, 6), num_simulari=1000)
    print("Numarul de bilete necâștigătoare până la primul câștigător pentru primele 10 simulări:",
          rezultate_simulare[:10])

    # ii) Estimarea probabilității pentru cel puțin 10 bilete succesive necâștigătoare
    probabilitate_estimata = np.mean(np.array(rezultate_simulare) >= 10)
    print("Estimarea probabilitatii pentru cel putin 10 bilete succesive necâștigătoare:", probabilitate_estimata)
    p=hypergeom.pmf(3,49,6,6)+hypergeom.pmf(4,49,6,6)+hypergeom.pmf(5,49,6,6)+hypergeom.pmf(6,49,6,6)
    # Calculul teoretic al probabilității
    probabilitate_teoretica = 1 - geom.cdf(9, p)
    print("Probabilitatea teoretica pentru cel putin 10 bilete succesive necâștigătoare:", probabilitate_teoretica)


main()
