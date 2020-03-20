'''
AND Gate
 x | y | o 
 0 | 0 | 0
 0 | 1 | 0
 1 | 0 | 0
 1 | 1 | 1

 0*w1 + 0*w2 + b = 0
 0*w1 + 1*w2 + b = 0
 1*w1 + 0*w2 + b = 0
 1*w1 + 1*w2 + b = 1

A X = B

 A = 0 0 1  X = w1  B = 0
     0 1 1      w2      0
     1 0 1      b       0
     1 1 1              1

 x*w1 + y*w2 + b = o
'''
import gd2 as gd
import numpy as np
from numpy.linalg import norm
    
A = np.array([[0, 1, 1], 
             [1, 0, 1], 
             [1, 1, 1]])
B = np.array([0.0, 0, 1]).transpose()

# def deriSig(x):
#     s = sig(x)
#     ds = s * (1 - s)
#     return ds

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

def f(p):
    X = p
    Y = np.dot(A, X)
    return norm(Y - B)

p = np.array([0.0, 0, 0])
# print(f(p))
p = gd.gradientDescendent(f, p)

print(p)
B = np.dot(A, p)
ans = []
for i in B:
    ans.append(0) if sig(i) <= 0.5 else ans.append(1)
print(ans)
