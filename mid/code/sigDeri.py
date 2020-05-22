import numpy as np
import matplotlib.pyplot as plt

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

def deriSig(x):
    s = sig(x)
    ds = s * (1 - s)
    return ds

t = np.arange(-10, 10, 0.01)

plt.plot(t, deriSig(t))
plt.title("Sigmoid derivation")
plt.show()