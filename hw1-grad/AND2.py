import numpy as np
from numpy.linalg import norm
    
A = np.array([[0.0, 0], 
             [0, 1], 
             [1, 0], 
             [1, 1]])
B = np.array([0.0, 0, 0, 1]).transpose()

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

def f(w, b):
    X = w
    Y = np.dot(A, X)
    print(Y)
    print(Y + b)
    return norm(Y + b)

w = np.array([1.0, 1])
b = -1
print(f(w, b))
