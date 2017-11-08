import random

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def trial(k, pi, pmax, n, m):
    '''Run a polya's urn simulation with n time-steps, m trials, k balls back,
        and p/pmax initial balls with class p. Returns average proportion of p
        over all trials.
    '''
    average = 0
    for i in range(m):
        p = pi
        for j in range(n + 1):
            if p >= random.randint(1, pmax + k*j):
                p += 1
        average += p/(pmax + k*(n + 1))
    return average/m

def simulate(kmax, pmax, n, m):
    ''' Iterate over trials with various inital conditions. Return a matrix of outcomes.
    '''
    data = np.zeros((pmax, kmax)) # Default float 64 is good.
    for k in range(kmax):
        for p in range(pmax):
            data[p, k] = trial(k, p, pmax, n, m)
    return data

def plot(data, pmax, kmax):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    X = []
    Y = []

    for i in range(kmax):
        for j in range(pmax):
            X.append(j)
    for i in range(pmax):
        for j in range(kmax):
            Y.append(i)

    Z = np.reshape(data, (pmax*kmax))
    print(Z)
    ax.scatter(X, Y, Z, c ='b', marker = 'o')

    plt.show()

data = simulate(100, 100, 5, 5)
plot(data, 100, 100)
