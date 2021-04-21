import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal

a = 25214903917
c = 11
m = 2 ** 48


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
    poblacion = normalizar(poblacion)
    return poblacion


def generador_gcl(seed, n):
    poblacion = [(a * seed + c) % m]
    for i in range(1, n):
        poblacion.append((a * poblacion[i-1] + c) % m)
    poblacion = normalizar(poblacion)
    return poblacion


def plot_pmc(seed1, seed2, n):
    x = generador_pmc(seed1, n)
    y = generador_pmc(seed2, n)

    sns.regplot(x=x, y=y, color='black', scatter_kws={'alpha': 0.4}, lowess=True)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def plot_gcl(seed1, seed2, n):
    x = generador_gcl(seed1, n)
    y = generador_gcl(seed2, n)

    sns.regplot(x=x, y=y, color='black', scatter_kws={'alpha': 0.4}, lowess=True)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def normalizar(a):
    minimo = min(a)
    maximo = max(a)
    arreglo = []
    for i in a:
        valor = (i - minimo)/(maximo - minimo)
        arreglo.append(valor)
    return arreglo


def chi_cuadrado(muestra):
    cant_celdas = 10
    celdas = contar_observ(muestra, cant_celdas)
    e = len(muestra)/cant_celdas
    chi = 0
    for o in celdas:
        chi += ((o - e) ** 2)/e
    print("grado de libertad: " + str(cant_celdas - 1))
    print("con un alfa de valor: 0.05")
    print("el valor obtenido es: " + str(chi))


def contar_observ(muestra, cant_celdas):
    step = Decimal(str(1/cant_celdas))
    min = 0
    max = step
    celdas = []
    ocurrencias = sum(map(lambda x: x <= max, muestra))
    celdas.append(ocurrencias)
    for i in range(1, cant_celdas):
        min += step
        max += step
        ocurrencias = sum(map(lambda x: min < x <= max, muestra))
        celdas.append(ocurrencias)
    return celdas


x = generador_gcl(9999, 1000)
chi_cuadrado(x)


"""
plot_pmc()
plot_gcl()"""
