import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal
import numpy as np
import pandas as pd
from termcolor import colored






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
    a = 25214903917
    c = 11
    m = 2 ** 48
    poblacion = [(a * seed + c) % m]
    for i in range(1, n):
        poblacion.append((a * poblacion[i-1] + c) % m)
    poblacion = normalizar(poblacion)
    return poblacion

def generador_cc(seed, z, n):
    a = 2 * z
    c = (2 * z) + 1
    m = 2 ** z
    for i in range(1,100):
        if (i-a)%4 == 1:
            b = i
            break
    poblacion = [(a * (seed ** 2) + b * seed + c) % m]
    for i in range(1, n):
        x = poblacion[i-1]
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
        valor = (i - minimo)/(maximo - minimo)
        arreglo.append(valor)
    return arreglo

def chi_cuadrado(muestra):
    df_chi = pd.read_excel("D:\GitHub\Trabajos-Simulacion\chi-cuadrado.xlsx")
    df_chi = pd.DataFrame(df_chi)
    cant_celdas = 10
    alpha = 0.05
    row = df_chi[df_chi[0] == cant_celdas - 1]
    valor = float(row[alpha])
    celdas = contar_observ(muestra, cant_celdas)
    e = len(muestra)/cant_celdas
    chi = 0
    for o in celdas:
        chi += ((o - e) ** 2)/e
    print(colored("PRUEBA DE BONDAD DE AJUSTE", "magenta"))
    if chi < valor:
        print(colored("La hipotesis nula es aceptada porque la prueba es menor que el valor crítico", "green"))
    else:
        print(colored("la hipotesis nula no es aceptada porque la prueba dio mayor al valor crítico", "red"))
    print(colored(str(chi), "blue") + ' < ' + str(valor))
    print("el valor obtenido es: " + colored(str(chi), "blue"))
    print("el valor critico con alpha= " +colored(str(alpha), "blue") + " y grado de libertad= " +
          colored(str(cant_celdas - 1), "blue") + " es el siguiente --> " + colored(str(valor), "blue"))


    x = ['Clase 1','Clase 2','Clase 3','Clase 4','Clase 5','Clase 6','Clase 7', 'Clase 8','Clase 9','Clase 10']
    # arregalr que no sea hardcodeado
    plt.bar(x,celdas)
    plt.show()

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

def runs_above_below(muestra):
    mean = np.mean(muestra)
    #a = sum(map(lambda x: x > mean, muestra))
    #b = sum(map(lambda x: x < mean, muestra))
    run = []
    a = 0
    b = 0
    for i in muestra:
        if i > mean:
            run.append(1)
            a += 1
        else:
            run.append(0)
            b += 1
    print(colored("PRUEBA DE NÚMEROS POR ENCIMA Y DEBAJO DE LA MEDIA", "magenta"))
    print("La media de la muestra es: " + colored(str(mean), "blue"))
    print("la cantidad total de números en la muestra es: "+ colored(str(len(muestra)), "blue"))
    print("La cantidad de números por debajo de la media es: "+ colored(str(b), "blue"))
    print("La cantidad de números por encima de la media es: " + colored(str(a), "blue"))
    var = range(len(run))
    plt.scatter(var, run, alpha=.25)
    plt.title("Test runs Above and Below")
    plt.xlim(0, len(run))
    plt.axhline(mean, color='red', label="media de la muestra")
    plt.xlabel("muestra n")
    plt.ylabel("valor de muestra")
    plt.legend()
    plt.show()

def reverse_arrangements(muestra):
    df_reverse = pd.read_excel("D:\GitHub\Trabajos-Simulacion\critical-arrangement.xlsx")
    df_reverse = pd.DataFrame(df_reverse)
    alpha = 0.025
    n = 100
    cont = 0
    row = df_reverse[df_reverse[0] == n]
    min = int(row[(1 - alpha)])
    max = int(row[alpha])
    for i in range(0,n-1):
        for j in range(i+1, n):
            if muestra[i] > muestra[j]:
                cont += 1
    print(colored("PRUEBA DE ARREGLOS INVERSOS ", "magenta"))
    if (min < cont) and (cont <= max):
        print(colored("La hipótesis nula es aceptada porque nuestro valor está dentro de los parámetros", "green"))
    else:
        print(colored("la hipótesis no es aceptada porque no cumple con los parámetros", "red"))
    print(str(min) + ' < ' + colored(str(cont), "blue") + ' <= ' + str(max))

seed1 = 4567
seed2 = 7891
#x = generador_cc(9849, 5,1000)
#x = generador_pmc(1234, 100)
x = generador_gcl(seed1, 1000)
y = generador_gcl(seed2, 1000)
chi_cuadrado(x)
print()
runs_above_below(x)
print()
reverse_arrangements(x)
print()
plot_(x, y)
