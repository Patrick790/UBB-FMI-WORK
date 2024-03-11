import numpy as np
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks, yticks, plot
from scipy.stats import uniform, expon

# Definirea distributiei de sange
grupe_sanguine = ['O', 'A', 'B', 'AB']
probabilitati = [0.46, 0.40, 0.10, 0.04]


def generare_aleatoare_discreta(N, valori, probabilitati):
    p0 = 0
    aleatorii = uniform.rvs(size=N)
    rezultate = []

    for u in aleatorii:
        for k in range(len(valori)):
            if p0 + sum(probabilitati[:k]) < u <= p0 + sum(probabilitati[:k+1]):
                rezultate.append(valori[k])
                break
    return rezultate


# Generare de N valori aleatoare pentru distributia discreta
N = 1000
aleatorii_discreti = generare_aleatoare_discreta(N, grupe_sanguine, probabilitati)

# Afisare frecventa relativa
frecventa = {grupa: aleatorii_discreti.count(grupa)/N for grupa in grupe_sanguine}
print("Frecventa relativa: ", frecventa)

# Afisare histograma
bar(grupe_sanguine, [frecventa[grupa] for grupa in grupe_sanguine], alpha=0.5, label='Simulare')
bar(grupe_sanguine, probabilitati, alpha=0.5, label='Teoretic')
legend()
show()

alpha = 1/12  # Parametrul distributiei Exponentiale

# Generare de N valori aleatoare pentru distributia continua Exponentiala
aleatorii_continue = -1/alpha * np.log(1 - uniform.rvs(size=N))

# Afisare histograma si functia de densitate
hist(aleatorii_continue, bins=12, density=True, range=(0, 60), alpha=0.7, label='Simulare')
x = np.linspace(0, 60, 100)
plot(x, expon.pdf(x, loc=0, scale=1/alpha), 'r-', label='Teoretic')
xticks(np.arange(0, 65, 5))
grid()
legend()
show()

# Estimarea probabilitatii evenimentului E: timpul de printare al afisului este cel putin 5 secunde
probabilitate_simulata = np.mean(aleatorii_continue >= 5)
probabilitate_teoretica = 1 - expon.cdf(5, loc=0, scale=1/alpha)

print(f"Probabilitatea simulata pentru timpul >= 5 secunde: {probabilitate_simulata}")
print(f"Probabilitatea teoretica pentru timpul >= 5 secunde: {probabilitate_teoretica}")


