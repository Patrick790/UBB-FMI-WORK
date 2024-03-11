
from random import sample
from math import perm,comb
from itertools import permutations, combinations

def permutari(n,k):
    perms = [''.join(p) for p in permutations(n,k)]
    return perms

def nr_total_permutari(n,k):
    return perm(len(n),k)

def perm_aleatoare(n,k):

    perms = permutari(n,k)
    return sample(perms, 1);

def combinari(n,k):
    combs = [''.join(p) for p in combinations(n,k)]
    return combs

def nr_total_combinari(n, k):
    return comb(len(n), k)

def combinare_random(n, k):
    perms = combinari(n, k)
    return sample(perms, 1)
def main():
    n = input("String: ")
    k = int(input("Adauga numar: "))
    print(permutari(n, k))
    print(nr_total_permutari(n,k))
    print(perm_aleatoare(n,k))
    print(combinari(n,k))
    print(nr_total_combinari(n,k))
    print(combinare_random(n,k))


main()
