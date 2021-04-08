import numpy as np
import random
import matplotlib.pyplot as plt

cant_nro = 37

list_fr = []
list_pr = []
list_ds = []
list_vr = []

x = list(range(cant_nro))


def calcula_frecuencia(total):
    fr = np.bincount(muestra) / total
    fr = fr.tolist()
    while len(fr) < cant_nro:
        fr.append(int(0))
    frecuencias.append(fr)


def ruleta():
    for i in range(1, tiradas):
        muestra.append(random.randint(0, cant_nro))
        calcula_frecuencia(i)
        promedios.append(np.mean(muestra))
        desvio.append(np.std(muestra))
        varianza.append(np.var(muestra))


def plot_promedios():
    plt.figure('PROMEDIOS')
    for i in range(0, poblacion):
        plt.plot(list_pr[i])
    prom_esp = sum(x)/cant_nro
    plt.axhline(prom_esp, label='Promedio espeado')
    plt.xlabel('n numero de tiradas')
    plt.legend()
    plt.show()


def plot_desvios():
    plt.figure('DESVIOS')
    for i in range(0, poblacion):
        plt.plot(list_ds[i])
    desv_esp = np.std(x)
    plt.xlabel('n numero de tiradas')
    plt.axhline(desv_esp, label='Desvio esperado')
    plt.legend()
    plt.show()


def plot_varianza():
    plt.figure('VARIANZA')
    for i in range(0, poblacion):
        plt.plot(list_vr[i])
    var_esp = np.var(x)
    plt.xlabel('n numero de tiradas')
    plt.axhline(var_esp, label='Varianza esperada')
    plt.legend()
    plt.show()


def plot_frecuencias(nro):
    fr = []
    for j in list_fr:
        aux = []
        for i in j:
            aux.append(i[nro])
        fr.append(aux)
    plt.figure('FRECUENCIA RELATIVA')
    plt.xlabel('n numero de tiradas')
    plt.title('Frecuencia Relativa del nro ' + str(nro))
    for i in range(0, poblacion):
        plt.plot(fr[i])
    plt.axhline(1 / 37, label='Frecuencia Relativa esperada')
    plt.legend()
    plt.show()


tiradas = int(input('Ingrese la cantidad de tiradas que desea realizar: '))
poblacion = int(input("ingrese tamaño de población: "))

for i in range(0, poblacion):
    frecuencias = []
    promedios = []
    desvio = []
    varianza = []
    muestra = []
    ruleta()
    list_fr.append(frecuencias)
    list_pr.append(promedios)
    list_ds.append(desvio)
    list_vr.append(varianza)
plot_promedios()
plot_desvios()
plot_varianza()
flag = 'S'
while flag == 'S':
    while True:
        i = int(input('Ingrese valor de 0 a 36 para estudiar su frecuencia: '))
        if (i >= 0) and (i <= 36):
            break
    plot_frecuencias(i)
    while True:
        flag = input('¿Desea consultar otro número? S/N ').upper()
        if flag == 'S' or flag == 'N':
            break