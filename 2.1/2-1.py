import matplotlib.pyplot as plt
import numpy as np

a = 25214903917
c = 11
m = 2**48


def completar_ceros(x):
    x = str(x)
    for _ in range(0, (8-len(x))):
        x = '0' + x
    return x


def generador_pmc(seed, n):
    poblacion = [seed]
    for i in range(1, n):
        x = poblacion[i-1]**2
        x = completar_ceros(x)
        seed = int(x[2:6])
        poblacion.append(seed)
    return poblacion


def generador_gcl(seed, n):
    poblacion = [(a * seed + c) % m]
    for i in range(1, n):
        poblacion.append((a * poblacion[i-1] + c) % m)
    return poblacion


def plot_pmc():
    x = generador_pmc(1234, 50)
    y = generador_pmc(5678, 50)

    plt.scatter(x, y, s=75, c='black', alpha=.25)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def plot_gcl():
    x = generador_gcl(9999, 1000)
    y = generador_gcl(8888, 1000)

    plt.scatter(x, y, s=75, c='black', alpha=.25)
    plt.xticks(())
    plt.yticks(())
    plt.show()


plot_pmc()
plot_gcl()
