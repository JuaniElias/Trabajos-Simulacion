import matplotlib.pyplot as plt
import seaborn as sns

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
    cant_clases = 10
    celdas = lambdas(muestra,cant_clases)
    e = len(muestra)/cant_clases
    chi = 0
    for o in celdas:
        chi += ((o-e)**2)/e
    print("grado de libertad: " + str(cant_clases-1))
    print("con un alfa de valor: 0.05")
    print("el valor obtenido es: "+ str(chi))

def lambdas(muestra, c):
    min = 0
    max = 1 / c
    celdas = []
    x = sum(map(lambda x: min <= x < max, muestra))
    celdas.append(x)
    for x in range(1, c):
        min += 1/c
        max += 1/c
        x = sum(map(lambda x: min < x <= max, muestra))
        celdas.append(x)
    celdas[9] += 1
    return celdas

x = generador_gcl(9999, 10000)
chi_cuadrado(x)


"""
plot_pmc()
plot_gcl()"""

