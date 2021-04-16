import matplotlib.pyplot as plt
import numpy as np



a = 25214903917
c = 11
m = 2**48

def generador_gcl(seed, n):
    poblacion = []
    poblacion.append((a * seed + c) % m)
    for i in range(1,n):
        poblacion.append((a * poblacion[i-1] + c) % m)
    return poblacion

def ajuste(x):
    x = str(x)
    for i in range(0, (8-len(x))):
        x = '0' + x
    return x

def generador_PMC(seed, n):
    poblacion = []
    poblacion.append(seed)
    for i in range(1, n):
        x = poblacion[i-1]**2
        x = ajuste(x)
        seed = int(x[2:6])
        poblacion.append(seed)
    return poblacion

def plot_gcl():
    x = generador_gcl(9999, 10000)
    y = generador_gcl(8888, 10000)
    plt.scatter(x, y, s=75, c='black', alpha=.25)
    plt.xticks(())
    plt.yticks(())
    plt.show()



plot_gcl()
