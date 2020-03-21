import gd2 as gd
import numpy as np
from numpy.linalg import norm
    
A = np.array([[0, 1, 1], 
             [1, 0, 1], 
             [1, 1, 1]])
B = np.array([0.0, 0, 1]).transpose()

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

def f(p):
    X = p
    Y = np.dot(A, X)
    return norm(Y - B)

p = np.array([0.0, 0, 0])
p = gd.gradientDescendent(f, p)

print("\n==================================================================================\n")

print("p = {}".format(p))

inputArr = np.array([[0, 0, 1], 
             [0, 1, 1],
             [1, 0, 1], 
             [1, 1, 1]])
B = np.dot(inputArr, p)



print("\nInputs: \n{}".format(inputArr))
print("A dot p = {}".format(B))
print("sig(B) = {}".format(sig(B)))
ans = []
for i in B:
    ans.append(0) if sig(i) <= 0.5 else ans.append(1)
    # ans.append(0) if sig(i) <= 0.6 else ans.append(1)
print("Output = {}".format(ans))

print("\n==================================================================================\n")
print("[w1, w2, b] = {}".format(p))
X = p.copy()
for i in range(len(p)):
    X[i] = round(p[i])
print("\nRounded weights & bias: {}".format(X))
print("--------------------------------")
print("\tInputs  |  Outputs")
for i in range(len(ans)):
    print("\t{}\t\t{}".format(inputArr[i], ans[i]))
