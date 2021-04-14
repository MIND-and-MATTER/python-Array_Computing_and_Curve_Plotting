# MATLAB - Functions, Plotting, and Matrices problems 2-4 using NumPy's diag function (Links to an external site.) to construct matrices and linalg.eig (Links to an external site.) function to find the eigenvalues and eigenvectors of a matrix.

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

a = 1+ np.ones(5)
m = np.diag(a)

for i in range(len(a)-1):
    m[i, i+1] = -1
    m[i+1, i]= -1


h = ((5+1)**2 / 2) * m

evals, evects = np.linalg.eig(h)

print(evals)

A = 1+ np.ones(10)
M = np.diag(A)

for i in range(len(A)-1):
    M[i+1, i] = -1
    M[i, i-1]= -1

H = ((10+1)**2 / 2) * m

Evals, Evects = np.linalg.eig(H)

print(Evals)



# H = ((5+1)^2 / 2) * m;

# [eigenvectors, eigenvalues] = eig(H);
# x_values = linspace(1/(5+1), 5/(5+1), 5);

# x = linspace(0,1);
# y2 = sqrt(2) * (sin(pi * x));

# plot(x_values, eigenvectors(:,1), "-", x, y2, "-." )