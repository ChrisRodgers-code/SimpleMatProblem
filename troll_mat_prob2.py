import numpy as np
from scipy.special import binom

n = 25

mat1 = np.array([[0.,0.,1.],[1.,0.,0.],[0.,1.,0.]])
mat2 = np.array([[0.,1.,0.],[0.,0.,1.],[1.,0.,0.]])
I    = np.identity(3, dtype = float)

var = np.zeros((3,3))
val = np.zeros((3,3))

for k in range(n+1):
	if(k%3 == 0):
		var = I
	elif(k%3 == 1):
		var = mat1
	elif(k%3 == 2):
		var = mat2
	val += binom(n,k)*var

print(val)
