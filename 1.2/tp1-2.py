import numpy as np
import matplotlib.pyplot as plt
import random

cant_nro = 37
rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

min_apuesta = 5
max_apuesta = 100


def ruleta(billetera):
    global fichas
    global max
    fichas = min_apuesta
    perdida = False
    if op == 3:
        suc = sucesion_fib(fichas)
        global indice
        indice = 0
    for i in range(1, tiradas):
        max_ = i
        if op == 1:
            fichas = martingala(perdida, fichas)
        elif op == 2:
            fichas = D_ALEMBERT(perdida, fichas)
        else:
            fichas = fibonacci(perdida, suc)
        if (fichas > max_apuesta) and inf == 'N' and fichas > billetera:
            break
        billetera -= fichas
        nro = random.randint(0, cant_nro)
        apuestas = apuesta()
        gan = ganancia(apuestas[1], apuestas[0], nro, fichas)
        if gan == 0:
            perdida = True
        elif nro == 0:
            perdida = False
            billetera += int(fichas / 2)
        else:
            perdida = False
            billetera += gan
        total_apuestas.append(billetera)
        if billetera <= fichas and inf == 'N':
            break
    if max_>max:
        max = max_


def martingala(flag, fichas):
    if flag:
        return fichas * 2
    else:
        return fichas


def D_ALEMBERT(flag, fichas):
    if flag:
        valor = fichas + 1
    elif fichas == min_apuesta:
        valor = fichas
    else:
        valor = fichas - 1
    return valor


def sucesion_fib(min):
    suc = [min, min]
    for i in range(2, int(tiradas * 0.25)):
        suc.append(suc[i - 1] + suc[i - 2])
    return suc


def fibonacci(flag, suc):
    global indice
    if flag:
        indice += 1
    elif (indice - 2) < 0:
        indice = 0
    else:
        indice -= 2
    return suc[indice]


def coin_flip():
    if random.randint(0, 1) == 0:
        return True
    else:
        return False


def paridad():
    apuesta = []
    if coin_flip():
        for i in range(2, 38, 2):
            apuesta.append(i)
    else:
        for i in range(1, 38, 2):
            apuesta.append(i)
    return apuesta


def color():
    if coin_flip():
        return rojo
    else:
        return negro


def half():
    if coin_flip():
        apuesta = list(range(1, 19))
    else:
        apuesta = list(range(19, 37))
    return apuesta


def ganancia(run, valor, nro, apuesta):
    if type(run) is list:
        if nro in run:
            profit = apuesta + (apuesta * valor)
        else:
            profit = 0
    else:
        if nro == run:
            profit = apuesta + (apuesta * valor)
        else:
            profit = 0
    return profit


def apuesta():
    nro = random.randint(1, 3)
    if nro == 1:
        apuesta = [1, color()]
    elif nro == 2:
        apuesta = [1, half()]
    else:
        apuesta = [1, paridad()]
    return apuesta


def plot_profit():
    plt.figure('Ganancias')
    plt.xlim([0, max+10])
    for i in range(0, poblacion):
        plt.plot(list_bi[i])
    caja = billetera
    plt.axhline(caja, label='valor inicial de caja')
    plt.xlabel('n numero de tiradas')
    plt.ylabel('Unidad monetaria')
    plt.legend()
    plt.grid()
    plt.show()



list_bi = []
max = 0
while True:
    print("1- Martingala" + '\n'
          "2- D’ALEMBERT" + '\n'
          "3- Fibonacci" + '\n')
    op = int(input())
    if (op >= 1) and (op <= 3):
        break
while True:
    inf = input("desea capital infito? S/N ").upper()
    if inf == 'S' or inf == 'N':
        if inf == 'N':
            billetera = int(input("ingrese el capital inicial: "))
        else:
            billetera = 0
        break
tiradas = int(input("ingrese la cantidad de tiradas: "))
poblacion = int(input("ingrese tamaño de población: "))
for i in range(0, poblacion):
    total_apuestas = [billetera]
    ruleta(billetera)
    list_bi.append(total_apuestas)
plot_profit()
