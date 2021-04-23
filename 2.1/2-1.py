import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal
import numpy as np
import pandas as pd
from termcolor import colored
import scipy.stats as ss
from datetime import datetime


def completar_ceros(x):
    x = str(x)
    for _ in range(0, (8 - len(x))):
        x = '0' + x
    return x


def generador_pmc(seed, n):
    poblacion = [seed]
    for i in range(1, n):
        x = poblacion[i - 1] ** 2
        x = completar_ceros(x)
        seed = int(x[2:6])
        poblacion.append(seed)
    poblacion = normalizar(poblacion)
    return poblacion


def generador_gcl(seed, n):
    a = 25214903917
    c = 11
    m = 2 ** 48
    poblacion = [(a * seed + c) % m]
    for i in range(1, n):
        poblacion.append((a * poblacion[i - 1] + c) % m)
    poblacion = normalizar(poblacion)
    return poblacion


def generador_cc(seed, z, n):
    a = 2 * z
    c = (2 * z) + 1
    m = 2 ** z
    for i in range(1, 100):
        if (i - a) % 4 == 1:
            b = i
            break
    poblacion = [(a * (seed ** 2) + b * seed + c) % m]
    for i in range(1, n):
        x = poblacion[i - 1]
        valor = (a * (x ** 2) + b * x + c) % m
        poblacion.append(valor)
    poblacion = normalizar(poblacion)
    return poblacion


def plot_(x, y):
    sns.regplot(x=x, y=y, color='black', scatter_kws={'alpha': 0.4}, lowess=True)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def normalizar(a):
    minimo = min(a)
    maximo = max(a)
    arreglo = []
    for i in a:
        valor = (i - minimo) / (maximo - minimo)
        arreglo.append(valor)
    return arreglo


def chi_cuadrado(muestra, cant_celdas):
    celdas = contar_observ(muestra, cant_celdas)
    e = len(muestra) / cant_celdas
    chi = 0
    for o in celdas:
        chi += ((o - e) ** 2) / e
    # Se crea la lista con los intervalos de las clases
    """divisiones = (list(map(lambda x: x / cant_celdas, range(1, cant_celdas + 1, 1))))
    divisiones = list(map(str, divisiones))

    plt.bar(divisiones, celdas)
    plt.xlabel("Clases")
    plt.ylabel("Frecuencias")
    plt.show()"""

    return chi


def contar_observ(muestra, cant_celdas):
    step = Decimal(str(1 / cant_celdas))
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


def runs_above_below(muestra):
    mean = np.mean(muestra)
    run = []
    a = 0
    b = 0
    c = 1
    for i in range(0, len(muestra)):
        if muestra[i] > mean:
            run.append(1)
            a += 1
        else:
            run.append(0)
            b += 1
    for i in range(1, len(run)):
        if run[i - 1] != run[i]:
            c += 1
    return a, b


def reverse_arrangements(muestra):
    cont = 0
    n = 100
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if muestra[i] > muestra[j]:
                cont += 1
    return cont


def fix_cont(cont):
    c = [0] * 5
    c[0] = cont[0]
    c[1] = cont[1]
    c[2] = cont[2]
    c[3] = cont[3]
    c[4] = cont[4] + cont[5] + cont[6]
    return c


def poker_test(muestra):
    contador = [0] * 7
    for i in range(0, len(muestra)):
        if muestra[i] == 1:
            m = str(int(muestra[i] * 10000))
        else:
            m = str(int(muestra[i] * 100000))
        poker = [0] * 5
        for j in range(0, len(m)):
            poker[j] = int(m[j])
        poker = np.bincount(poker)
        par = pok = trio = gene = 0
        for p in poker:
            if p == 2:
                par += 1
            elif p == 3:
                trio = 1
            elif p == 4:
                pok = 1
            elif p == 5:
                gene = 1
        if par == trio == 1:
            contador[4] += 1  # full
        elif par == 2:
            contador[2] += 1  # par doble
        elif par == 1:
            contador[1] += 1  # par simple
        elif trio == 1:
            contador[3] += 1  # trio
        elif pok == 1:
            contador[5] += 1  # poker
        elif gene == 1:
            contador[6] += 1  # generala
        else:
            contador[0] += 1  # todos diferentes
    return fix_cont(contador)


def estudio_chi2():
    cant_celdas = 10
    chi = 0
    # Uso scipy para calcular el chi cuadrado
    valor = ss.chi2.ppf(1 - alpha, (cant_celdas - 1) * lon)
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = generador_cc(seed,56, lon_muestra)
        chi += chi_cuadrado(serie, cant_celdas)
    print(colored("PRUEBA DE BONDAD DE AJUSTE", "magenta"))
    if chi < valor:
        print(colored("La hipótesis nula es aceptada porque la prueba es menor que el valor crítico", "green"))
    else:
        print(colored("la hipótesis nula NO es aceptada pues no se cumple", "red"))
    print(colored(str(chi), "blue") + ' < ' + str(valor))
    print("el valor obtenido es: " + colored(str(chi), "blue"))
    print("el valor critico con alpha= " + colored(str(alpha), "blue") + " y grado de libertad= " +
          colored(str((cant_celdas - 1) * lon), "blue") + " es el siguiente --> " + colored(str(valor), "blue"))
    print()


def estudio_AaBM():
    a = b = 0
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = generador_cc(seed,56, lon_muestra)
        c, d = runs_above_below(serie)
        a += c
        b += d
    mu = ((2 * a * b) / a + b) + 1
    va = 2 * a * b * (2 * a * b - (a + b)) / (a + b - 1) * (a + b) ** 2
    norm = ss.norm(0, 1)
    z1 = (b - mu) / np.sqrt(va)
    z2 = 1 - (alpha / 2)
    print(colored("PRUEBA DE NÚMEROS POR ENCIMA Y DEBAJO DE LA MEDIA", "magenta"))
    if (norm.cdf(z1)) >= (norm.cdf(z2)):
        print(colored("Se rechaza la hipótesis de aleatoriedad puesto que se cumple", "red"))
    else:
        print(colored("Se aprueba la hipótesis de aleatoriedad puesto que NO se cumple", "green"))
    print(colored(str(norm.cdf(z1)), "blue") + ' >= ' + str(norm.cdf(z2)))
    print()


def estudio_RA():
    df_reverse = pd.read_excel("critical-arrangement.xlsx")
    df_reverse = pd.DataFrame(df_reverse)
    n = 100
    cont = 0
    row = df_reverse[df_reverse[0] == n]
    min = int(row[(1 - alpha / 2)])
    max = int(row[alpha / 2])
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = generador_cc(seed,56, lon_muestra)
        cont += reverse_arrangements(serie)
    print(colored("PRUEBA DE ARREGLOS INVERSOS ", "magenta"))
    if (min < cont / lon) and (cont / lon <= max):
        print(colored("La hipótesis nula es aceptada porque nuestro valor pues se cumple", "green"))
    else:
        print(colored("la hipótesis no es aceptada porque no cumple", "red"))
    print(str(min) + ' < ' + colored(str(cont / lon), "blue") + ' <= ' + str(max))
    print()


def estudio_poker():
    prob = [0.3024 * lon_muestra * lon, 0.5040 * lon_muestra * lon, 0.1080 * lon_muestra * lon,
            0.072 * lon_muestra * lon,
            0.0090 * lon_muestra * lon + 0.0045 * lon_muestra * lon + 0.0001 * lon_muestra * lon]
    contador = [0] * 5
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = generador_cc(seed, 56, lon_muestra)
        cont = poker_test(serie)
        for j in range(0, len(contador)):
            contador[j] += cont[j]
    parametro = 0
    for i in range(0, len(contador)):
        parametro += ((prob[i] - contador[i]) ** 2) / prob[i]
    grad_lib = len(contador) - 1
    chi = ss.chi2.ppf(1 - alpha, grad_lib)
    print(colored("PRUEBA DE POKER ", "magenta"))
    if parametro < chi:
        print(colored("Se acepta la hipotesis de que los números están ordenados al azar pues", "green"))
    else:
        print(colored("No se acepta la hipotesis de que los números están ordenados al azar pues no se cumple", "red"))
    print(colored(str(parametro), "blue") + ' <= ' + str(chi))


seed1 = 1111
seed2 = 7891
lon_muestra = 1000
lon = 30
alpha = 0.05

estudio_chi2()
estudio_AaBM()
estudio_RA()
estudio_poker()
x = generador_gcl(seed1, lon_muestra)
y = generador_gcl(seed2, lon_muestra)

plot_(x, y)
