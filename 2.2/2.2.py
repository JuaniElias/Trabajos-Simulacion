import math
import random
import numpy as np
import scipy.stats as ss


def dist_uni(a, b, r):
    x = a + (b - a) * r
    return x

def dist_exp(media, r):
    x = - media * np.log(r)
    return x

def dist_gamma(media, r, a, k):
    x = 0
    if media % 2 == 0:
        for i in range(0,k):
            x += (-1/a) * np.log(r[i])
    else:
        ki = 0
        for i in range(0,k):
            ki += (r[i] - k/2)
        z = ki / np.sqrt(k/12)
        for i in range(0,k):
            x += (-1/a) * np.log(r[i])
        x += z ** 2
    return x

def dist_norm(mu, sigma, k, r):
    ki = 0
    for i in range(0,k):
        ki += (r[i] - k/2)
    x = (sigma * ((12/k) ** (1/2)) ) * ki + mu

    return x

def dist_chi2(a, m, k, r):
    x = 0
    if m % 2 == 0:
        for i in range(0,k):
            x += (-1/a) * np.log(r[i])
    elif m < 30:
        ki = 0
        for i in range(0, k):
            ki += (r[i] - k / 2)
        z = ki / np.sqrt(k / 12)
        for i in range(0, k):
            x += (-1 / a) * np.log(r[i])
        x += z ** 2
    else:
        chi = ss.chi2(1 - a, m)
        z = np.sqrt(chi) - np.sqrt(2 * m) - 1
        x = ((z + np.sqrt(2 * m - 1)) ** 2) / 2
    return x

def dist_logn(mu, sigma, k, r):
    z = 0
    for i in range(0, k):
        z += (r[i] - (k / 2))
    x = np.exp(mu + sigma * ((k/12) ** (-1/2)) * z)
    return x

def dist_geom(r, p):
    q = 1 - p
    x = math.log10(r)/math.log10(q)
    return int(x)

def dist_pascal(mu, sigma, r):
    p = mu/sigma
    k = (mu ** 2)/(sigma - mu)
    ki = 0
    if type(k) == int:
        for i in range(0, k):
            ki += math.log10(r[i])
        x = ki / math.log10(1 - p)
    else:
        x = 0 # no entiendos
    return x

def dist_binom(mu, sigma, r):
    p = (mu - sigma)/mu
    n = int((mu ** 2)/(mu - sigma))
    x = [0]
    for i in range(1, n):
        if r[i] <= p:
            x.append(x[i-1] + 1)
        else:
            x.append(x[i - 1])
    return x[n-1]

def dist_hiperg():
    #i  duno bru, explanation is kinda lame
    return 0

def dist_poisson():
    #same
    return 0

