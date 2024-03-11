import math
import random
from random import randint

import numpy.random
from math import dist
import matplotlib.pyplot as plt
from numpy.random import randint


# 1a
def simulari_grup(n, nr_sim):
    c = 0
    for i in range(nr_sim):
        birthdays = [randint(1, 365) for i in range(n)]

        if len(birthdays) != len(set(birthdays)):
            c += 1

    probabilitate = c / nr_sim

    return probabilitate


# 1b
def probabilitate_zi_de_nastere(n):
    probabilitate = 1.0
    for i in range(n):
        probabilitate *= (365 - i) / 365
    # probabilitatea complementara
    return 1 - probabilitate

def generate_points(N):
    points = [(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)) for _ in range(N)]
    return points

def is_inside_circle(point):
    # Verificăm dacă un punct este în interiorul cercului de rază 0.5 și centru în (0, 0).
    return math.sqrt(point[0] ** 2 + point[1] ** 2) <= 0.5

def is_closer_to_center_than_vertices(point):
    # Verificăm dacă un punct este mai aproape de centrul pătratului decât de vârfurile acestuia.
    return abs(point[0]) <= 0.25 and abs(point[1]) <= 0.25



def geometric_probability_inside_circle(raza, latura):
    # Probabilitatea geometrică pentru puncte în interiorul cercului
    return math.pi * (raza ** 2) / (latura ** 2)

def geometric_probability_closer_to_center(lungime_centru, latura):
    # Probabilitatea geometrică pentru puncte mai aproape de centrul pătratului
    return (lungime_centru / latura) ** 2



def main():
    n = 23
    probabilitate_cel_putin_doua = probabilitate_zi_de_nastere(n)
    print(
        f"Probabilitatea ca cel puțin două persoane dintr-un grup de {n} să aibă aceeași zi de naștere este: {probabilitate_cel_putin_doua:.4f}")
    nr_pers = int(input("Numar persoane: "))
    simulari = int(input("Numar simulari: "))
    nr = simulari_grup(nr_pers, simulari)
    print(nr)

    N_values = [500, 1000, 2000]

    for N in N_values:
        points = generate_points(N)

        # (i) Numărul de puncte în interiorul cercului
        points_inside_circle = [point for point in points if is_inside_circle(point)]
        relative_frequency_inside_circle = len(points_inside_circle) / N

        # (ii) Numărul de puncte mai aproape de centrul pătratului decât de vârfurile acestuia
        points_closer_to_center = [point for point in points if is_closer_to_center_than_vertices(point)]
        relative_frequency_closer_to_center = len(points_closer_to_center) / N

        # acute_triangles, obtuse_triangles = count_triangles(points)
        # relative_frequency_acute_triangles = acute_triangles / (N * (N - 1) * (N - 2) / 6)
        # relative_frequency_obtuse_triangles = obtuse_triangles / (N * (N - 1) * (N - 2) / 6)

        prob_inside_circle = geometric_probability_inside_circle(0.5, 1)
        prob_closer_to_center = geometric_probability_closer_to_center(0.25, 1)


        print(f'N = {N}')
        print(
            f'Frecventa relativa din interiorul cercului: {relative_frequency_inside_circle:.4f} Probabilitate geometrică: {prob_inside_circle:.4f}')
        print(
            f'Frecventa relativa mai aproape de centru: {relative_frequency_closer_to_center:.4f} Probabilitate geometrică: {prob_closer_to_center:.4f}')


main()
