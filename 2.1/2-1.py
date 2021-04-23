import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal
import numpy as np
import pandas as pd
from termcolor import colored
import scipy.stats as ss

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
    cant_celdas = 10
    alpha = 0.05
    valor = ss.chi2.ppf(1-alpha, cant_celdas - 1)
    celdas = contar_observ(muestra, cant_celdas)
    e = len(muestra)/cant_celdas
    chi = 0
    for o in celdas:
        chi += ((o - e) ** 2)/e
    print(colored("PRUEBA DE BONDAD DE AJUSTE", "magenta"))
    if chi < valor:
        print(colored("La hipotesis nula es aceptada porque la prueba es menor que el valor crítico", "green"))
    else:
        print(colored("la hipotesis nula NO es aceptada pues no se cumple", "red"))
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
    alpha = 0.05
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
    for i in range(1,len(run)):
        if run[i-1] != run[i]:
            c += 1
    mu = ((2*a*b)/a+b)+1
    va = 2*a*b*(2*a*b - (a+b))/(a+b-1)*(a+b)**2
    x = ss.norm(0,1)
    z1 = (b - mu)/np.sqrt(va)
    z2 = 1 - (alpha/2)

    print(colored("PRUEBA DE NÚMEROS POR ENCIMA Y DEBAJO DE LA MEDIA", "magenta"))
    if (x.cdf(z1)) >= (x.cdf(z2)):
        print(colored("Se rechaza la hipotésis de aleatoriedad puesto que se cumple", "red"))
    else:
        print(colored("Se aprueba la hipotesis de aleatoriedad puesto que NO se cumple", "green"))
    print(colored(str(x.cdf(z1)), "blue") + ' >= ' + str(x.cdf(z2)))
    print("La media de la muestra es: " + colored(str(mean), "blue"))
    print("la cantidad total de números en la muestra es: "+ colored(str(len(muestra)), "blue"))
    print("La cantidad de números por debajo de la media es: "+ colored(str(b), "blue"))
    print("La cantidad de números por encima de la media es: " + colored(str(a), "blue"))

def reverse_arrangements(muestra):
    df_reverse = pd.read_excel("critical-arrangement.xlsx")
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
        print(colored("La hipótesis nula es aceptada porque nuestro valor pues se cumple", "green"))
    else:
        print(colored("la hipótesis no es aceptada porque no cumple", "red"))
    print(str(min) + ' < ' + colored(str(cont), "blue") + ' <= ' + str(max))

def fix_cont(cont):
    c = [0] * 5
    c[0] = cont[0]
    c[1] = cont[1]
    c[2] = cont[2]
    c[3] = cont[3]
    c[4] = cont[4] + cont[5] + cont[6]
    return c

def poker_test(muestra, n):
    prob = [0.3024 * n, 0.5040 * n, 0.1080 * n, 0.072 * n, 0.0090 * n + 0.0045 * n + 0.0001 * n]
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
    contador = fix_cont(contador)
    parametro = 0
    for i in range(0, len(contador)):
        parametro += ((prob[i] - contador[i]) ** 2) / prob[i]
    alpha = 0.05
    grad_lib = len(contador) - 1
    chi = ss.chi2.ppf(1 - alpha, grad_lib)
    print(colored("PRUEBA DE POKER ", "magenta"))
    if parametro < chi:
        print(colored("Se acepta la hipotesis de que los números están ordenados al azar pues", "green"))
    else:
        print(colored("No se acepta la hipotesis de que los números están ordenados al azar pues", "red"))

    print(colored(str(parametro), "blue") + ' <= ' + str(chi))




seed1 = 1111
seed2 = 7891
n = 1000
#x = generador_cc(9849, 5,1000)
#x = generador_pmc(1234, 100)
x = generador_cc(seed1,66, n)
y = generador_cc(seed2,90, n)
chi_cuadrado(x)
print()
runs_above_below(x)
print()
reverse_arrangements(x)
print()
poker_test(x,n)
plot_(x, y)
