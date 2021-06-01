import random
import os
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


def generador_python(seed, n):
    random.seed(seed)
    poblacion = []
    for i in range(0, n):
        poblacion.append(random.random())
    return poblacion

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


def generador_cc(seed, g, n):
    a = 2 * g
    c = (2 * g) + 1
    m = 2 ** g
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


def plot_hist(celdas):
    cant_celdas = 10
    # Se crea la lista con los intervalos de las clases
    divisiones = (list(map(lambda x: x / cant_celdas, range(1, cant_celdas + 1, 1))))
    divisiones = list(map(str, divisiones))
    plt.title("Gráfico de barras de frecuencias en la prueba de Chi Cuadrado")
    for i in range(0, lon):
        plt.bar(divisiones, celdas[i], alpha=1/10)
    plt.xlabel("Clases")
    plt.ylabel("Frecuencias")
    plt.show()


def plot_poker(a, b):
    clases = ["Diferentes", "Par", "Par doble", "Trio", "Full-House", "Poker", "Quintilla"]
    for i in range(0, len(b)):
        b[i] *= lon_muestra
    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    fig.suptitle("Gráfico de barras de frecuencias en la prueba de poker")
    for i in range(0, lon):
        ax1.bar(clases, a[i], alpha=1/10)
    ax2.bar(clases, b)
    ax1.set_title("Valores Observados por cada muestra")
    ax2.set_title("Valor Esperados por muestra")
    plt.show()


def chi_cuadrado(muestra, cant_celdas):
    celdas = contar_observ(muestra, cant_celdas)
    e = len(muestra) / cant_celdas
    chi = 0
    for o in celdas:
        chi += ((o - e) ** 2) / e
    return chi, celdas


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
    c = [0] * 6
    c[0] = cont[0]
    c[1] = cont[1]
    c[2] = cont[2]
    c[3] = cont[3]
    c[4] = cont[4]
    c[5] = cont[5] + cont[6]
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
    return contador


def estudio_chi2(op):
    cant_celdas = 10
    chi = 0
    df_clases = []
    # Uso scipy para calcular el chi cuadrado
    valor = ss.chi2.ppf(1 - alpha, (cant_celdas - 1) * lon)
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = valida(op, lon_muestra, seed)
        aux, clases = chi_cuadrado(serie, cant_celdas)
        chi += aux
        df_clases.append(clases)
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
    plot_hist(df_clases)


def estudio_AaBM(op):
    a = b = 0
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = valida(op, lon_muestra, seed)
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


def estudio_RA(op):
    df_reverse = pd.read_excel("critical-arrangement.xlsx")
    df_reverse = pd.DataFrame(df_reverse)
    n = 100
    cont = 0
    row = df_reverse[df_reverse[0] == n]
    min = int(row[(1 - alpha / 2)])
    max = int(row[alpha / 2])
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = valida(op, lon_muestra, seed)
        cont += reverse_arrangements(serie)
    print(colored("PRUEBA DE ARREGLOS INVERSOS ", "magenta"))
    if (min < cont / lon) and (cont / lon <= max):
        print(colored("La hipótesis nula es aceptada porque nuestro valor pues se cumple", "green"))
    else:
        print(colored("la hipótesis no es aceptada porque no cumple", "red"))
    print(str(min) + ' < ' + colored(str(cont / lon), "blue") + ' <= ' + str(max))
    print()


def estudio_poker(op):
    prob = [0.3024, 0.5040, 0.1080, 0.072, 0.0090, 0.0045, 0.0001]
    contador = [0] * 7
    graf = []
    for i in range(0, lon):
        seed = int(str(datetime.now().time())[-4:])
        serie = valida(op, lon_muestra, seed)
        cont = poker_test(serie)
        graf.append(cont)
        for j in range(0, len(contador)):
            contador[j] += cont[j]
    parametro = 0
    for i in range(0, len(contador)):
        fe = (prob[i] * lon_muestra * lon)
        parametro += ((fe - contador[i]) ** 2) / fe
    grad_lib = len(contador) - 1
    chi = ss.chi2.ppf(1 - alpha, grad_lib)
    print(colored("PRUEBA DE POKER ", "magenta"))
    if parametro < chi:
        print(colored("Se acepta la hipotesis de que los números están ordenados al azar pues", "green"))
    else:
        print(colored("No se acepta la hipotesis de que los números están ordenados al azar pues no se cumple", "red"))
    print(colored(str(parametro), "blue") + ' <= ' + str(chi))
    plot_poker(graf, prob)

def valida(opcion, longitud, seed):
    if opcion == 1:
        serie = generador_pmc(seed, longitud)
    elif opcion == 2:
        serie = generador_gcl(seed, longitud)
    elif opcion == 3:
        serie = generador_cc(seed, 56, longitud)
    else:
        serie = generador_python(seed, longitud)
    return serie

lon_muestra = 1000
lon = 60
alpha = 0.05
flag = True
while flag:
    print("")
    print(colored("Estudios para:", "green"))
    print("1. Generador middle-square")
    print("2. Generador GCL")
    print("3. Generador GCC")
    print("4. Generador Python")
    print("")
    op = int(input(colored("Ingrese generador que quiera estudiar: ","blue")))
    print("")
    estudio_chi2(op)
    estudio_AaBM(op)
    estudio_RA(op)
    estudio_poker(op)
    seed1 = random.randint(1000, 9999)
    seed2 = random.randint(1000, 9999)
    x = valida(op, 5000, seed1)
    y = valida(op, 5000, seed2)
    plot_(x, y)
    print("")
    x = input(colored("Desea realizar otro estudiar? S/N    ", "red")).upper()
    if x == 'N':
        flag = False