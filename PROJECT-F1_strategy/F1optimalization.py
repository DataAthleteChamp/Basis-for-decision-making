import numpy as np
import pyswarms as ps

sredni_czas_okrazenia_S = 10
sredni_czas_okrazenia_M = 10.5
sredni_czas_okrazenia_H = 11.0
N = 50
petrol = 90.0
tpit = 2.5
zuzycie_paliwa_S = np.array(
    [0.9, 0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72,
     0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53,
     0.52, 0.51, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41])

zuzycie_paliwa_M = np.array(
    [0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72, 0.71, 0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62,
     0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52, 0.51, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43,
     0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31])
zuzycie_paliwa_H = np.array(
    [0.7, 0.69, 0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.6, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52,
     0.51, 0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33,
     0.32, 0.31, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21])
kara_S = np.array(
    [0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15,
     15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23])
kara_M = np.array(
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8,
     8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11])
kara_H = np.array(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
     5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7])
scieranie_S = 5
scieranie_M = 7
scieranie_H = 9

def f(x):
    for particle in x:
        xS, xM, xH, pitstop_S, pitstop_M, pitstop_H = map(int, np.rint(particle))

        czas = xS * sredni_czas_okrazenia_S + xM * sredni_czas_okrazenia_M + xH * sredni_czas_okrazenia_H
        czas += (pitstop_S + pitstop_M + pitstop_H) * tpit

        kara = np.sum(kara_S[:xS]) + np.sum(kara_M[:xM]) + np.sum(kara_H[:xH])
        czas += kara
        return czas


# Ograniczenia
lb = [0, 0, 0, 0, 0, 0]
ub = [N, N, N, N // scieranie_S, N // scieranie_M, N // scieranie_H]

constraints = (np.array(lb), np.array(ub))

# Optymalizacja rojem cząstek
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=constraints)

# Wykonywanie optymalizacji
best_cost, best_pos = optimizer.optimize(f, 8000)  # Maksymalnie 1000 iteracji

print("Najlepsze rozwiązanie: ", np.rint(best_pos), ", koszt: ", best_cost)
