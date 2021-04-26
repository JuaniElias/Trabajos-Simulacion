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
        z = 0
        for i in range(0,k):
            z += (r[i] - k/2)/np.sqrt(k/12)
        for i in range(0,k):
            x += (-1/a) * np.log(r[i]) + z ** 2
    return x

def dist_norm(mu, sigma, k, r):
    x = 0
    for i in range(0,k):
        x += (sigma * ((12/k) ** (1/2)) ) * (r[i] - k/2) + mu
    return x

def dist_chi2(a, m, k, r):
    x = 0
    if m % 2 == 0:
        for i in range(0,k):
            x += (-1/a) * np.log(r[i])
    elif m < 30:
        z = 0
        for i in range(0, k):
            z += (r[i] - k / 2) / np.sqrt(k / 12)
        for i in range(0,k):
            x += (-1/a) * np.log(r[i]) + z ** 2
    else:
        chi = ss.chi2(1 - a, m)
        z = np.sqrt(chi) - np.sqrt(2 * m) - 1
        x = ((z + np.sqrt(2 * m - 1)) ** 2) / 2
    return x

def dist_logn(mu, sigma, k, r):
    for i in range(0, k):
        z += (r[i] - k / 2) / np.sqrt(k / 12)
    x = np.exp(mu + sigma * ((k/12) ** (-1/2)) * z)
    return x