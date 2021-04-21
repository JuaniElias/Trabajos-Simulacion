import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal
import numpy as np
import pandas as pd

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
    if chi < valor:
        print("La hipotesis nula es aceptada porque la prueba es menor que el valor crítico")
    else:
        print("la hipotesis nula no es aceptada porque la prueba dio mayor al valor crítico")
    print("el valor obtenido es: " + str(chi))
    print("el valor critico con alpha= " + str(alpha) + " y grado de libertad= " + str(
        cant_celdas - 1) + " es el siguiente --> " + str(valor))
    print(str(chi) + '<' + str(valor))

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
    print("La media de la muestra es: " + str(mean))
    print("la cantidad total de números en la muestra es: "+ str(len(muestra)))
    print("La cantidad de números por debajo de la media es: "+ str(b))
    print("La cantidad de números por encima de la media es: " + str(a))
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

    if (min < cont) and (cont <= max):
        print("La hipótesis nula es aceptada porque nuestro valor está dentro de los parámetros")
    else:
        print("la hipótesis no es aceptada porque no cumple con los parámetros")
    print(str(min) + '<' + str(cont) + '<=' + str(max))


x = generador_gcl(9999, 1000)
chi_cuadrado(x)
runs_above_below(x)
reverse_arrangements(x)




"""
plot_pmc()
plot_gcl()"""
