import math
import random
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import seaborn as sns


def dist_uni(a, b):
    r = random.random()
    x = a + (b - a) * r
    return x

def dist_exp(media):
    r = random.random()
    x = - media * np.log(r)
    return x

def dist_gamma(media, var):
    k = int((media**2)/var)
    a = media/var
    r = np.random.random(k)
    if media % 2 == 0:
        ri = np.prod(r)
        x = (-1/a) * np.log(ri)
    elif k==1:
        x = dist_exp(media)
    else:
        ki = sum(r)
        z = (ki - k/2) / np.sqrt(k/12)
        ri = np.prod(r)
        x = (-1 / a) * np.log(ri) + z**2
    return x

def dist_norm(mu, sigma, k):
    r = np.random.random(k)
    ki = sum(r)
    x = (sigma * (np.sqrt(12/k)) * (ki- k/2)) + mu
    return x


def dist_binom(mu, sigma):
    p = (mu - sigma)/mu
    n = int((mu ** 2)/(mu - sigma))
    r = np.random.random(n)
    x = 0
    for i in range(0, n):
        if r[i] <= p:
            x += 1
    return x

def dis_binom2(n, p):
    r = np.random.random(n)
    x = 0
    for i in range(0, n):
        if r[i] <= p:
            x += 1
    return x

def dist_hiperg(Ne, n, p):
    x = 0
    r = np.random.random(n)
    for i in range(1, n):
        if r[i-1] <= p:
            s = 1
            x += 1
        else:
            s = 0
        p = ((Ne * p) - s) / (Ne - 1)
        Ne -= 1
    return x

def dist_poisson(l):
    x = 0
    b = np.exp(-l)
    ri = random.random()
    while ri > b:
        x += 1
        ri *= random.random()
    return x

def dist_disc():
    return 0

def prueba_uni():
    uni_py = np.random.uniform(0,50,10000)
    uni_sus = []
    for i in range(10000):
        uni_sus.append(dist_uni(0,50))
    ax = sns.histplot(data=uni_py,
                      binwidth=0.5,
                      color='blue',
                      alpha=0.5,
                      label='Generador Python')
    ab = sns.histplot(data=uni_sus,
                      binwidth=0.5,
                      color='red',
                      alpha=0.5,
                      label='Generado por nuestro código')
    ax.set(xlabel='Distribución Uniforme', ylabel='Frecuencia')
    plt.legend()
    plt.show()

def prueba_exp():
    exp_py = np.random.exponential(1/10,10000)
    exp_sus = []
    for i in range(0,10000):
        exp_sus.append(dist_exp(1/10))
    ax = sns.histplot(data= exp_py,
                      binwidth=0.005,
                      color='blue',
                      alpha=0.5,
                      label='Generador Python')
    ab = sns.histplot(data= exp_sus,
                      binwidth=0.005,
                      color='red',
                      alpha=0.5,
                      label= 'Generado por nuestro código')
    ax.set(xlabel='Distribución Exponencial', ylabel='Frecuencia')
    plt.legend()
    plt.show()

def prueba_normal():
    norm_py = ss.norm.rvs(loc=10, scale=3, size=10000 )
    norm_sus = []
    for i in range(10000):
        norm_sus.append(dist_norm(10,3,12))
    ax = sns.histplot(data=norm_py,
                      binwidth=0.1,
                      color='blue',
                      alpha=0.5,
                      label='Generador Python')
    ab = sns.histplot(data=norm_sus,
                      binwidth=0.1,
                      color='red',
                      alpha=0.5,
                      label='Generado por nuestro código')
    ax.set(xlabel='Distribución Normal', ylabel='Frecuencia')
    plt.legend()
    plt.show()

def prueba_bin():
    bin_py = np.random.binomial(50,0.10,10000)
    bin_sus = []
    for i in range(10000):
        bin_sus.append(dis_binom2(50, 0.1))
    x = range(0,len(np.bincount(bin_py)))
    plt.bar(x,np.bincount(bin_py),
             alpha=0.5,
             color='blue',
             label='Generador Python'
    )
    x = range(0, len(np.bincount(bin_sus)))
    plt.bar(x, np.bincount(bin_sus),
             alpha=0.5,
             color='red',
             label='Generado por nuestro código'
             )
    plt.xlabel('Distribución Binomial')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.show()

def prueba_poisson():
    poisson_py = ss.poisson.rvs(mu=5, size=10000)
    poisson_sus = []
    for i in range(10000):
        poisson_sus.append(dist_poisson(5))
    x = range(0, len(np.bincount(poisson_py)))
    plt.bar(x, np.bincount(poisson_py),
            alpha=0.5,
            color='blue',
            label='Generador Python'
            )
    x = range(0, len(np.bincount(poisson_sus)))
    plt.bar(x, np.bincount(poisson_sus),
            alpha=0.5,
            color='red',
            label='Generado por nuestro código'
            )
    plt.xlabel('Distribución de Poisson')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.show()



prueba_uni()
prueba_exp()
prueba_normal()
prueba_bin()
prueba_poisson()