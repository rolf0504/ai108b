import numpy as np
import matplotlib.pyplot as plt

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

t = np.arange(-10, 10, 0.1)

plt.plot(t, sig(t))
plt.title("Sigmoid")
plt.show()