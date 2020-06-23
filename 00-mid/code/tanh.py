import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    s = np.tanh(x)
    return s

t = np.arange(-10, 10, 0.1)

plt.plot(t, relu(t))
plt.title("tanh")
plt.show()