import numpy as np
from scipy.special import binom

n = 25

mat = np.array([[0.,0.,1.],[1.,0.,0.],[0.,1.,0.]])
I   = np.identity(3, dtype = float)

val = np.zeros((3,3))

var = I
for k in range(n+1):
	val += binom(n,k)*var
	var = np.dot(var,mat)

print(val)
