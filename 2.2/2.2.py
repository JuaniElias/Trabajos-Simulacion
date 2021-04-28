import math
import random
import numpy as np
import scipy.stats as ss


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
        x = dist_exp(media, r[0])
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

def dist_pascal(mu, sigma):
    p = mu/sigma
    k = float((mu ** 2)/(sigma - mu))
    if not(k.is_integer()) and random.random() <= .5:
        k = int(k)
    else:
        k = int(k) + 1
    k = int(k)
    r = np.random.random(k)
    ki = np.prod(r)
    x = np.log(ki) / np.log(1 - p)
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

def dis_binom2(p,n):
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
x = []
for i in range(0,23):
    x.append(dist_poisson(5))
print(x)
print(np.random.poisson(5,23))
