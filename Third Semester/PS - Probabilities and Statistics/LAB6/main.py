from scipy.stats import norm, expon, uniform
from numpy import mean, std, linspace, multiply, exp
from matplotlib.pyplot import show, hist, grid, legend, xticks, plot
import numpy as np
from scipy.integrate import quad

# Simularea inaltimii persoanelor
n_values = [1000, 2000, 5000]
m = 165  # medie
sigma = 10  # deviatie standard

for n in n_values:
    heights = norm.rvs(loc=m, scale=sigma, size=n)

    # Histograma si densitatea
    hist(heights, bins=16, density=True, range=(130, 210), color='lightblue', edgecolor='black')
    x = linspace(130, 210, 100)
    plot(x, norm.pdf(x, loc=m, scale=sigma), 'r-', lw=2)

    # Afisare
    show()

    # Calculul mediei, deviatiei standard si proportiei in intervalul [160, 170]
    mean_value = mean(heights)
    std_value = std(heights)
    proportion = sum((heights >= 160) & (heights <= 170)) / n

    print(f"n = {n}")
    print(f"Medie: {mean_value:.2f}")
    print(f"Deviatie standard: {std_value:.2f}")
    print(f"Proportia in intervalul [160, 170]: {proportion:.4f}")
    print("------------")

# Problema 2

# a)
data = []

for i in range(0,10000):
    random_num = np.random.random()
    if random_num<=0.4:
        data.append(expon.rvs(loc=0,scale=5, size = 1))
    else:
        data.append(uniform.rvs(loc=4,scale=2,size=1))

print(f"Medie:{np.mean(data)}")
print(f"Deviatie standard:{np.std(data)}")

# b)
pb_practica = np.sum([1 for i in data if i<5])/ len(data)
print(f"Probabilitatea practica ca timpul <5s: {pb_practica}")

# c)
pb_teoretica = 0.4*expon.cdf(5,loc=0,scale=5) + 0.6 * 1/2

print(f"Probabilitatea  teoretica ca timpul <5s: {pb_teoretica}")

# Problema 3

# Definirea functiei g(x)
def g(x):
    return exp(-x ** 2)


# Setarea intervalului [a, b]
a = -1
b = 3
n_simulations = 10000

# Generarea de valori aleatoare uniforme
u_values = uniform.rvs(loc=a, scale=b-a, size=n_simulations)

# Calculul valorilor g(u) pentru fiecare valoare generata
g_values = g(u_values)

# Estimarea integralei folosind metoda Monte Carlo
integral_approximation = (b - a) * mean(g_values)

print(f"Aproximarea Monte Carlo a integralei: {integral_approximation:.4f}")
print(quad(g, -1, 3)[0])
